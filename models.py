from app import db

class PullRequest(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    author_name = db.Column(db.String(255))
    author_email = db.Column(db.String(255))
    link = db.Columt(db.String(255))
    approvals = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    ready_for_review = db.Column(db.Boolean)

    def __init__(self, *args, **kwargs):
        super(PullRequest, self).__init__(*args, **kwargs)