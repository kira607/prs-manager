from db_client import DbClient
from mail_client import MailClient
from typing import Tuple

class Service:
    def __init__(self):
        self.db_client = DbClient()
        self.mail_client = MailClient()

    def get_table() -> Tuple[dict, int]:
        code = 200
        try:
            response = DbClient.get_table()
        except Exception as e:
            msg = f"Could not load table. Error: {e}"
            response = __make_error_response()
            code = 500
        return response, code

    def webhook() -> Tuple[dict, int]:
        pass

    def __make_error_response(msg: str, code: int) -> dict:
        return {
            "error": f"{msg}",
            "code": code
        }