# !-*- encoding=utf-8 -*-
"""
    common.oauth_provider.py
    ~~~~~~~~~~~~~~~~~~

    OAuth Server

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, jsonify
from werkzeug.security import safe_str_cmp

from common.app import jwt

auth = Blueprint('auth', __name__, url_prefix='/auth')


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


@jwt.authentication_handler
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


@jwt.identity_handler
def identify(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


@jwt.jwt_error_handler
def error_handler(error):
    from collections import OrderedDict
    return jsonify(OrderedDict([
        ('message', error.error),
        ('description', error.description),
    ])), error.status_code, error.headers


# def payload_handler(identity):
#     return {'user_id': identity.id}
