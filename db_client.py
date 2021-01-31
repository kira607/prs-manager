from MySQLdb import _mysql as mysql 


class DbClient:
    def __init__(self):
        client = mysql.connect()

    def get_table(self) -> dict:
        return {"table status": "empty"}

    def update(self, data: dict) -> None:
        pass

