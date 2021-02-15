from MySQLdb import _mysql as mysql
import os


class DbClient:
    def __init__(self):
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        passwd = os.getenv('DB_PASSWORD')
        db = os.getenv('DB_NAME')
        self.client = mysql.connect(host=host, user=user, passwd=passwd, db=db)

    def get_table(self) -> dict:
        return {"table status": "empty"}

    def update(self, data: dict) -> None:
        pass

if __name__ == '__main__':
    client = DbClient()
    print(client.get_table())