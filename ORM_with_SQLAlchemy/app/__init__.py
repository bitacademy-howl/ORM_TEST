from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:stark1234@localhost/webdb?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'manyrandombyte'

db = SQLAlchemy(app)

from ORM_with_SQLAlchemy.app.models import *

db.create_all()