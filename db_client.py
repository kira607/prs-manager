from flask_sqlalchemy import SQLAlchemy
from app import db
from models import PullRequests


class DbClient:
    def __init__(self):
        self.db = db
        # self.db.create_all()
        # self.session = db.session

    def get_table(self) -> dict:
        pull_requests = PullRequests.query.all()
        return pull_requests

    def update(self, data: dict) -> None:
        pass

    def insert(self):
        # self.session.add(data)
        # self.session.commit()
        pass

if __name__ == '__main__':
    client = DbClient()
    print(client.get_table())