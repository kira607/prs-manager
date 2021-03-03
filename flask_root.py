from flask import Flask, request, make_response
# from flask_admin import Admin
from service import Service

app = Flask(__name__)

# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# admin = Admin(app, name='prs-manager')

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
