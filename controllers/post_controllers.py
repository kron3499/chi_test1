from flask import Blueprint, request
from sqlalchemy.testing.pickleable import User

from app import db
from model.post import Post
from model.users import Users
from token_required import token_required

post_control: Blueprint = Blueprint('posts', __name__, url_prefix='/posts')

@post_control.route('/')
@token_required
def get_post():

    return 'Hello'

@post_control.route('/', methods=['POST'])
def create_post(self, user_id, title, body, created):
    title = request.json.get("title")
    body = request.json.get("body")
    user_id = request.json.get("userId")

    user = User.query.filter(User.id == id).first()

    post = Post()
    post.title = title
    post.body = body
    post.created = user_id

    db.db.session.add(post)
    db.session.commit()
    return post


@post_control.route("/users/<user_id>", methods=['DELETE'])
def delete_post(user_id):
    user = Users.query.filter(Users.id == id).first()

    User.query.filter(User.id == id).delete()

    return "Delete all posts"