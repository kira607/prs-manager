from flask import Flask, request
import git

app = Flask(__name__)

@app.route('/pull_updates', methods=['POST'])
def pull_updates():
    if request.method == 'POST':
        repo = git.Repo('.')
        origin = repo.remotes.origin
        origin.pull()
        return 'Update server: success', 200
    else:
        return 'Wrong request type', 400

@app.route('/')
def main():
    return 'Hello World!'
