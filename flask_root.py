from flask import Flask, request
from update_validator import is_valid_signature
import git
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    x_hub_signature = request.headers.get('X-Hub-Signature')
    if not is_valid_signature(x_hub_signature, request.data, str(os.getenv('SECRET_TOKEN'))):
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
    return 'Hello World 6'
