from datetime import datetime

from sqlalchemy import func

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=func.now())
    user_id = db.Column(db.Integer)
