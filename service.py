from db_client import DbClient
from mail_client import MailClient
from flask import request as flask_request
from update_validator import is_valid_signature
import git
import os
from typing import Tuple, Union

class Service:
    def __init__(self, db_client: DbClient):
        self.SECRET_TOKEN = os.getenv('SECRET_TOKEN')
        self.db_client = db_client
        self.mail_client = MailClient()

    def hello(self) -> Tuple[Union[dict, str], int]:
        code = 200
        try:
            with open("html/hello.html", "r") as f:
                response = f.read()
        except Exception as e:
            msg = f"Could not load hello. Error: {e}"
            response = __make_error_response()
            code = 500
        return response, code

    def get_table(self) -> Tuple[Union[dict, str], int]:
        code = 200
        try:
            data = self.db_client.get_table()
            with open("html/table.html", "r") as f:
                content = f.read()
            # merge data with page
            response = content
        except Exception as e:
            msg = f"Could not load table. Error: {e}"
            response = __make_error_response()
            code = 500
        return response, code

    def webhook(self, request: flask_request) -> Tuple[Union[dict, str], int]:
        code = 200
        x_hub_signature = request.headers.get('X-Hub-Signature')
        if self.SECRET_TOKEN is None:
            code = 500
            msg = "Update server: failed (secret token is not configured)"
            response = self.__make_error_response(msg, code)
        elif not is_valid_signature(x_hub_signature, request.data, self.SECRET_TOKEN):
            code = 404
            msg = "Invalid token, deploy aborted."
            response = self.__make_error_response(msg, code)
        elif request.method == 'POST':
            repo = git.Repo('.')
            origin = repo.remotes.origin
            origin.pull()
            response = 'Update server: success'
        else:
            code = 400
            response = 'Wrong request type'
        return response, code

    def __make_error_response(self, msg: str, code: int) -> dict:
        return {
            "error": f"{msg}",
            "code": code
        }