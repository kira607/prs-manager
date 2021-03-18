from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from config import FlaskAppConfig

app = Flask(__name__)
app.config.from_object(FlaskAppConfig)
db = SQLAlchemy(app)

