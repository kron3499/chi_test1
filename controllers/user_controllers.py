import datetime

import jwt
from flask import Blueprint, jsonify, request, make_response
from pip._internal.network import auth
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, app
from model.users import Users

user_control: Blueprint = Blueprint('users', __name__)


@user_control.route('/register', methods=['POST'])
def signup_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(name=data['name'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'registered successfully'})


@user_control.route('/login', methods=['POST'])
def login_user():
    auth = request.get_json()
    print(auth)
    if not auth or not auth['username'] or not auth['password']:
        return make_response('could not verify', 401, {'Authentication': 'login required"'})

    user = Users.query.filter_by(name=auth['username']).first()
    print(auth, auth['password'])
    if check_password_hash(user.password, auth['password']):
        token = jwt.encode(
            {'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            app.config['SECRET_KEY'], "HS256")

        return jsonify({'token': token})

    return make_response('could not verify', 401, {'Authentication': '"login required"'})



