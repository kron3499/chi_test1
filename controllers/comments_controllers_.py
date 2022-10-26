from tokenize import Comment

from flask import Blueprint, request

from app import db
from model import comment
from model.users import Users

comments_control: Blueprint = Blueprint('comments', __name__, url_prefix='/comments')


@comments_control.route("/users/<user_id>", methods=['POST'])
def create_comment(user_id):
    comment_value = request.json.get("comment")

    user = Users.query.filter(Users.id == id).first()

    if not user:
        return "User not found", 400

    comment = Comment()
    comment.comment = ''.join(reversed(comment_value))
    comment.user_id = user_id

    db.session.add(comment)
    db.session.commit()

    return comment


@comments_control.route("/users/<user_id>", methods=['GET'])
def get_comment(user_id):
    user = Users.query.filter(Users.id == user_id).first()

    if not user:
        return "User not found", 400

    db.session.add(comment)
    db.session.commit()

    return comment


@comments_control.route("/users/<user_id>", methods=['DELETE'])
def delete_comment(user_id):
    user = Users.query.filter(Users.id == user_id).first()

    if not user:
        return "user not found", 400

    Comment.query.filter(Comment.user_id == user_id).delete()

    db.session.commit()

    return "Delete all comments"


@comments_control.route("/<comment_id>", methods=['DELETE'])
def delete_comment_byid(comment_id):
    Comment.query.filter(Comment.id == comment_id).first()
    if not comment:
        return "wrong comment id", 400

    Comment.query.filter(Comment.id == comment_id).first()

    return "comment delete"
