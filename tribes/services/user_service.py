# !-*- encoding=utf-8 -*-
"""
    services.user.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint, jsonify, make_response, request
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

    args = request.get_json()
    user_dao.edit_user_name(user_id, args['name'])

    return make_response(get(user_id), 201)


@users.route('/<user_id>', methods=['DELETE'])
def delete(user_id):
    """DELETE /users/<user_id>
    根据用户id删除用户
    """
    if not _check_existed(user_id):
        return make_error(404, message='user not found')
    user_dao.delete_user_by_id(user_id)

    return make_response('', 204)


@users.route('/', methods=['GET'])
def all_user():
    """GET /users/
    获取所有用户
    """
    return jsonify(user_dao.find_all())


@users.route('', methods=['POST'])
def post():
    """POST /users/
        新建用户
    """
    args = request.get_json()
    # TODO(du_zhi_qiang@163.com): 新建需要返回主键.
    user_id = user_dao.insert_user(args['name'])
    return make_response(jsonify({'id': user_id}), 201)
