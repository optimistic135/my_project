from exts import db
from datetime import datetime

class usermode(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

class words(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    English = db.Column(db.String(255))
    Chinese = db.Column(db.String(255))

class learning(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20))
    English = db.Column(db.String(255))
    Chinese = db.Column(db.String(255))
    join_time = db.Column(db.DateTime, default=datetime.now)