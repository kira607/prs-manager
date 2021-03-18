import os

from flask import request, make_response

from app import app, db
from service import Service

service = Service()


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