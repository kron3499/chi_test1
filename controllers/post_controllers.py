from flask import Blueprint, request, jsonify
from pip._internal.network import auth


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

    db.session.add(post)
    db.session.commit()
    return jsonify({'post.id': post.id})



