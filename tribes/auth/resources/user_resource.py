# !-*- encoding=utf-8 -*-
"""
    Resource.user_resource.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""

from auth.dao import user_dao
from flask import jsonify
from flask_restful import Resource

# from common.exceptions import ValidationError


class UserResource(Resource):
    """/user/<user_id>
    根据id操作用户
    """

    def get(self, user_id):
        """GET ／user/<user-id>
        根据用户id查找用户基本信息
        """
        result = user_dao.find_user_by_id(user_id)
        return jsonify({'id': result['id'], 'name': result['name']})

    def put(self, user_id):
        """PUT /user/<user_id>
        根据id更新用户信息
        """
        pass

    def delete(self, user_id):
        """delete /user/<user_id>
        根据用户id删除用户
        """
        pass
