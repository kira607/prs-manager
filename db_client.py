from flask_sqlalchemy import SQLAlchemy


class DbClient:
    def __init__(self, db: SQLAlchemy):
        self.db = db
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