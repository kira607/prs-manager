from app import db

class PullRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    author_name = db.Column(db.String(255))
    author_email = db.Column(db.String(255))
    link = db.Column(db.String(255))
    approvals = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    ready_for_review = db.Column(db.Boolean)

    def __init__(self, *args, **kwargs):
        super(PullRequests, self).__init__(*args, **kwargs)

    def __repr__(self):
        return str(self.dict())

    def dict(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'author_name': self.author_name, 
            'author_email': self.author_email, 
            'link': self.link, 
            'approvals': self.approvals, 
            'created_date': self.created_date, 
            'ready_for_review': self.ready_for_review, 
        }