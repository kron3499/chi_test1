from sqlalchemy import func

from app import db


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer)
    liked = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=func.now())
    like_user_id = db.Column(db.Integer)