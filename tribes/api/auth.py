# !-*- encoding=utf-8 -*-
"""
    common.oauth_provider.py
    ~~~~~~~~~~~~~~~~~~

    OAuth Server

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, request

from common.app import jwt
from common.response import make_login_error, make_result
from service import user_service

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@jwt.authentication_handler
def authenticate(username, password):
    """身份认证方法"""
    from common.utils import verify_password
    user = user_service.find_user_by_login_name(username)
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
    return make_login_error(error.error, error.description), error.status_code, error.headers


@auth.route('/verify_email/<email>', methods=['GET'])
def verify_email(email):
    """验证邮箱是否有效"""
    return make_result({'is_valid': user_service.check_email(email)})


@auth.route('/signup', methods=['POST'])
def sign_up():
    """注册新用户"""
    args = request.get_json()

    user_id = user_service.add_user(
        args['email'], args['name'], args['password'])

    return make_result({'id': user_id})

# @auth.route('/active_account/<active_code>', methods=['GET'])
# def active_account(active_code):
#     """账号激活接口
#     active_code 加密激活码需解码为用户邮箱，回调地址
#     """
#     pass
