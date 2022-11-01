from flask import Blueprint, request, jsonify
from sqlalchemy.sql.functions import user

from app import db
from model.post import Post
from model.users import Users
from token_required import token_required

post_control: Blueprint = Blueprint('posts', __name__, url_prefix='/posts')



@post_control.route('/', methods=['POST'])
@token_required
def create_post(current_user):
    title = request.json.get("title")
    body = request.json.get("body")
    post = Post(title=title, body=body, user_id=current_user.id)

    db.db.session.add(post)
    db.session.commit()
    return jsonify({'post.id': post.id})


@post_control.route("/users/<user_id>", methods=['DELETE'])
def delete_post(user_id):
    user = Users.query.filter(Users.id == id).first()

    User.query.filter(User.id == id).delete()

    return "Delete all posts"
