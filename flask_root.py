from flask import Flask, request, make_response
from service import Service

app = Flask(__name__)

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
    return 'Hello World! webhook test r'
