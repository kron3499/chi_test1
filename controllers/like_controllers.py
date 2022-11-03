from flask import Blueprint, request, jsonify
from sqlalchemy import and_

from app import db
from model.like import Like
from model.post import Post
from token_required import token_required

like_control: Blueprint = Blueprint('like', __name__, url_prefix='/likes')


@like_control.route('/<post_id>', methods=['POST'])
@token_required
def create_like(current_user, post_id):
    liked = request.json.get("liked")
    post = Post.query.filter(Post.id == post_id).first()
    if not post:
        return "post not found", 400
    if not liked:
        like = Like.query.filter(and_(Like.post_id == post_id, Like.like_user_id == current_user.id)).delete()
    else:
        like = Like(post_id=post_id, like_user_id=current_user.id, liked=liked)

        db.session.add(like)
        db.session.commit()

        return jsonify({'like.id': like.id})
