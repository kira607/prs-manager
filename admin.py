from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import PullRequests
from db_client import DbClient as dbc

from app import app

admin = Admin()
db = dbc()
admin.add_view(ModelView(PullRequests, db.get_session()))