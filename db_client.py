from flask_sqlalchemy import SQLAlchemy
from app import db
from models import PullRequests


class DbClient:
    def __init__(self):
        self.db = db
        # self.db.create_all()

    def get_table(self) -> list:
        pull_requests = PullRequests.query.all()
        return pull_requests

    def update(self, data: dict) -> None:
        pass

    def get_session(self):
        return self.db.session

    def insert(self):
        # self.session.add(data)
        # self.session.commit()
        pass
