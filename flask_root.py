from flask import Flask, request
from update_validator import is_valid_signature
import git
import os

app = Flask(__name__)

SECRET_TOKEN = os.getenv('SECRET_TOKEN')

@app.route('/webhook', methods=['POST'])
def webhook():
    x_hub_signature = request.headers.get('X-Hub-Signature')
    if SECRET_TOKEN is None:
        print("Secret is None. Deploy failed...")
        return "Update server: failed (secret token is not configured)", 500
    else:
        if not is_valid_signature(x_hub_signature, request.data, SECRET_TOKEN):
            print("Deploy failed")
    if request.method == 'POST':
        repo = git.Repo('.')
        origin = repo.remotes.origin
        origin.pull()
        return 'Update server: success', 200
    else:
        return 'Wrong request type', 400

@app.route('/')
def main():
    return 'Hello World! webhook test'
