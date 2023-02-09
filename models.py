from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(25), nullable=False)
    reg_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"User {self.name}"

