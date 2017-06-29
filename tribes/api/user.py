# !-*- encoding=utf-8 -*-
"""
    api.user.py
    ~~~~~~~~~~~~~~~~~~

    用户管理相关的所有接口.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, request

from common.authenticate import jwt_required
from common.response import make_result
from service import user_service

user = Blueprint('user', __name__, url_prefix='/api/user')


@user.route('/<user_id>', methods=['GET'])
@jwt_required()
def get(user_id):
    """GET ／user/<user-id>
    根据用户id查找用户基本信息
    """
    result = user_service.find_user_by_id(int(user_id))
    return make_result(result)


@user.route('/<user_id>', methods=['PUT'])
@jwt_required()
def put(user_id):
    """PUT /users/<user_id>
        根据id更新用户信息
    """
    args = request.get_json()

    return make_result(user_service.update_user_name(user_id, args['name']))


@user.route('/<user_id>', methods=['DELETE'])
@jwt_required()
def delete(user_id):
    """DELETE /users/<user_id>
    根据用户id删除用户
    """
    return make_result(user_service.delete_user(user_id))


@user.route('/all', methods=['GET'])
@jwt_required()
def all_user():
    """GET /users/
    获取所有用户
    """
    return make_result(user_service.find_all_user())
