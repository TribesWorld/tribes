# !-*- encoding=utf-8 -*-
"""
    services.user.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, jsonify
from dao import user_dao

from common.error_handler import make_error

users = Blueprint('users', __name__)


def _check(user_id):
    if user_dao.is_user_existed(user_id) is False:
        return False
    else:
        return True


@users.route('/user/<user_id>', methods=['GET'])
def get(user_id):
    """GET ／users/<user-id>
    根据用户id查找用户基本信息
    """
    if not _check(user_id):
        return make_error(404, message='user not found')

    result = user_dao.find_user_by_id(user_id)
    return jsonify(result)
