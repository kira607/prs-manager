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
    page = """
<!DOCTYPE html>

<head>
    <title>Hello</title>
</head>

<body>
    <h1>Hello</h1>
</body>
    """
    return make_response(page, 200)
    # return 'Hello World! webhook test r'
