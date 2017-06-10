# !-*- encoding=utf-8 -*-
"""
    common.oauth_provider.py
    ~~~~~~~~~~~~~~~~~~

    OAuth Server

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, jsonify, request, make_response

from common.app import jwt
from common.error_handler import make_error
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
            'account_name': user['account_name'],
            'email': user['email'],
            'status': user['status']
        }


@jwt.identity_handler
def identity(payload):
    """返回当前用户身份信息"""
    user = payload['identity']
    return user


@jwt.jwt_error_handler
def error_handler(error):
    """身份认证异常处理"""
    from collections import OrderedDict
    return jsonify(OrderedDict([
        ('message', error.error),
        ('description', error.description),
    ])), error.status_code, error.headers


@auth.route('/verify_email/<email>', methods=['GET'])
def verify_email(email):
    """验证邮箱是否有效"""
    return make_response(jsonify({'is_valid': user_dao.is_email_existed(email)}), 200)


@auth.route('/signup', methods=['POST'])
def sign_up():
    """注册新用户"""
    from common.utils import encode_password
    args = request.get_json()

    # 检查用户邮箱是否存在
    if user_dao.is_email_existed(args['email']):
        return make_error(202, message='email already existed.')
    user_id = user_dao.insert_user(
        args['name'], encode_password(args['password']), args['email'])

    from services.mail_service import send_verify_email

    send_verify_email(args['name'], args['email'])
    return make_response(jsonify({'id': user_id}), 201)
