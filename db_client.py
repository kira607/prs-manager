from flask_sqlalchemy import SQLAlchemy
from app import app


class DbClient:
    def __init__(self, db: SQLAlchemy):
        self.db = SQLAlchemy(app)
        db.create_all()
        self.session = db.session

    def get_table(self) -> dict:
        return {"table status": "empty"}

    def update(self, data: dict) -> None:
        pass

    def insert(self):
        # self.session.add(data)
        # self.session.commit()
        pass

if __name__ == '__main__':
    client = DbClient()
    print(client.get_table())