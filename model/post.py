from datetime import datetime

import args as args
import kwargs as kwargs
from sqlalchemy.sql.functions import now

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(50))
    body = db.Column(db.Text)
    created = db.Column(db.DataTime, default=datetime(now))


def __repr__(self):
    return '<id {}>'.format(self.id)



