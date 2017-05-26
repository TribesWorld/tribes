# !-*- encoding=utf-8 -*-
"""
    Resource.user_resource.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import jsonify
from flask_restful import Resource, reqparse

from common.error_handler import make_api_error
from common.service import api
from dao import user_dao

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


@api.resource('/users/<user_id>')
class UserResource(Resource):
    """/users/<user_id>
    根据id操作用户
    """

    def get(self, user_id):
        """GET ／users/<user-id>
        根据用户id查找用户基本信息
        """
        self._check(user_id)
        result = user_dao.find_user_by_id(user_id)

        return result

    def put(self, user_id):
        """PUT /users/<user_id>
        根据id更新用户信息
        """
        self._check(user_id)
        args = parser.parse_args()
        new_name = args['name']
        user_dao.edit_user_name(user_id, new_name)

        return self.get(user_id), 201

    def delete(self, user_id):
        """DELETE /users/<user_id>
        根据用户id删除用户
        """
        self._check(user_id)
        user_dao.delete_user_by_id(user_id)

        return '', 204

    def _check(self, user_id):
        if user_dao.is_user_existed(user_id) is False:
            make_api_error(404, description='user not found')


@api.resource('/users/')
class UserListResource(Resource):
    """
    操作用户
    """

    def get(self):
        """GET /users/
        获取所有用户
        """
        return user_dao.find_all()

    def post(self):
        args = parser.parse_args()
        args = parser.parse_args()
        name = args['name']
        # temp
        user_dao.insert_user(name)
        return jsonify({'1': '1'}), 201

    def _check(self, user_id):
        if user_dao.is_user_existed(user_id) is True:
            make_api_error(400, description='user already exist')
