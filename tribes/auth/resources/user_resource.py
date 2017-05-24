from common.exceptions import ValidationError

from flask import jsonify
from flask_restful import Resource
from common.service import db
from auth.dao import user_dao


class UserResource(Resource):
    def get(self, user_id):
        result = user_dao.find_user_by_id(user_id)
        return jsonify({'id': result['id'], 'name': result['name']})
