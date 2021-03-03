from flask import Flask, request, make_response
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from service import Service
import os

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
passwd = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

class FlaskAppConfig:
    FLASK_ADMIN_SWATCH = 'cerulean'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{passwd}@{host}/{db_name}'

app = Flask(__name__)
app.config.from_object(FlaskAppConfig)

admin = Admin(app, name='prs-manager')
db = SQLAlchemy(app)
db_client = DbClient(db)
service = Service(db_client)


@app.route('/table', methods=['GET'])
def get_table():
    resp, code = service.get_table()
    response = make_response(resp, code)
    return response


@app.route('/webhook', methods=['POST'])
def webhook():
    resp, code = service.webhook(request)
    response = make_response(resp, code)
    return response


@app.route('/')
def main():
    resp, code = service.hello()
    response = make_response(resp, code)
    return response
