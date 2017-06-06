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
from dao import user_dao

auth = Blueprint('auth', __name__, url_prefix='/auth')


@jwt.authentication_handler
def authenticate(username, password):
    """身份认证方法"""
    from common.utils import verify_password
    user = user_dao.find_user_by_login_name(username)
    if user and verify_password(password, user['password_hash']):
        return {
            'id': user['id'],
            'account_name': user['account_name']
        }


@jwt.identity_handler
def identity(payload):
    user = payload['identity']
    return user


@jwt.jwt_error_handler
def error_handler(error):
    from collections import OrderedDict
    return jsonify(OrderedDict([
        ('message', error.error),
        ('description', error.description),
    ])), error.status_code, error.headers
