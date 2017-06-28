# !-*- encoding=utf-8 -*-
"""
    api.user.py
    ~~~~~~~~~~~~~~~~~~

    用户管理相关的所有接口.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, jsonify, make_response, request
from common.authenticate import jwt_required
from common.database import database
from common.error_handler import make_error
from service import user_service

user = Blueprint('user', __name__, url_prefix='/api/user')


# @users.route('/<user_id>', methods=['GET'])
# @jwt_required()
# def get(user_id):
#     """GET ／users/<user-id>
#     根据用户id查找用户基本信息
#     """
#     if not _check_existed(user_id):
#         return make_error(404, message='user not found')

#     result = user_dao.find_user_by_id(user_id)
#     return jsonify(result)


# @users.route('/<user_id>', methods=['PUT'])
# @jwt_required()
# def put(user_id):
#     """PUT /users/<user_id>
#         根据id更新用户信息
#     """
#     if not _check_existed(user_id):
#         return make_error(404, message='user not found')

#     args = request.get_json()
#     user_dao.edit_user_name(user_id, args['name'])

#     return make_response(get(user_id), 201)


# @users.route('/<user_id>', methods=['DELETE'])
# @jwt_required()
# def delete(user_id):
#     """DELETE /users/<user_id>
#     根据用户id删除用户
#     """
#     if not _check_existed(user_id):
#         return make_error(404, message='user not found')
#     user_dao.delete_user_by_id(user_id)

#     return make_response('', 204)


@user.route('/all', methods=['GET'])
# @jwt_required()
def all_user():
    """GET /users/
    获取所有用户
    """
    return jsonify(user_service.find_all_user())
