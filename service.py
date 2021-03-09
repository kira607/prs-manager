import git
import os
import hmac
import hashlib

from db_client import DbClient
from mail_client import MailClient
from flask import request as flask_request, render_template
from typing import Tuple, Union


class Service:
    def __init__(self):
        self.SECRET_TOKEN = os.getenv('SECRET_TOKEN')
        self.db_client = DbClient()
        self.mail_client = MailClient()

    def hello(self) -> Tuple[Union[dict, str], int]:
        code = 200
        try:
            response = render_template('hello.html')
        except Exception as e:
            msg = f"Could not load hello. Error: {e}"
            response = self.__make_error_response()
            code = 500
        return response, code

    def get_table(self) -> Tuple[Union[dict, str], int]:
        code = 200
        try:
            data = self.db_client.get_table()
            response = render_template('table.html', prs=data)
        except Exception as e:
            code = 500
            msg = f"Could not load table. Error: {e}"
            response = self.__make_error_response(msg, code)
        return response, code

    def webhook(self, request: flask_request) -> Tuple[Union[dict, str], int]:
        code = 200
        x_hub_signature = request.headers.get('X-Hub-Signature')
        if self.SECRET_TOKEN is None:
            code = 500
            msg = "Update server: failed (secret token is not configured)"
            response = self.__make_error_response(msg, code)
        elif not self.__is_valid_signature(x_hub_signature, request.data, self.SECRET_TOKEN):
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

    @staticmethod
    def __is_valid_signature(x_hub_signature, data, private_key):
        hash_algorithm, github_signature = x_hub_signature.split('=', 1)
        algorithm = hashlib.__dict__.get(hash_algorithm)
        encoded_key = bytes(private_key, 'latin-1')
        mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
        return hmac.compare_digest(mac.hexdigest(), github_signature)