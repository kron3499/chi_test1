from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(100))
    user_id = db.Column(db.Integer())

    def __repr__(self):
        return '<id {}>'.format(self.id)
