# !-*- encoding=utf-8 -*-
"""
    services.user.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, jsonify, make_response, request, current_app
from dao import user_dao

from common.error_handler import make_error

users = Blueprint('users', __name__, url_prefix='/users')


def _check_existed(user_id):
    return user_dao.is_user_existed(user_id)


@users.route('/<user_id>', methods=['GET'])
def get(user_id):
    """GET ／users/<user-id>
    根据用户id查找用户基本信息
    """
    if not _check_existed(user_id):
        return make_error(404, message='user not found')

    result = user_dao.find_user_by_id(user_id)
    return jsonify(result)


@users.route('/<user_id>', methods=['PUT'])
def put(user_id):
    """PUT /users/<user_id>
        根据id更新用户信息
    """
    if not _check_existed(user_id):
        return make_error(404, message='user not found')

    current_app.logger.info(request.get_json())
    reqargs = request.get_json()
    user_dao.edit_user_name(user_id, reqargs['name'])

    return make_response(get(user_id), 201)
