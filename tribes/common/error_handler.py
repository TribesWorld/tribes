# !-*- encoding=utf-8 -*-
"""
通用错误封装

error.py create by v-zhidu
"""
from flask import make_response, jsonify


class ErrorHandler(object):
    """
    通用错误封装
    """

    @staticmethod
    def bad_request(message):
        result = {'error': 'bad request', 'msg': message}
        return make_response(jsonify(result), 400)

    @staticmethod
    def unauthorized(message):
        result = {'error': 'unauthorized', 'msg': message}
        return make_response(jsonify(result), 401)

    @staticmethod
    def forbidden(message):
        result = {'error': 'forbidden', 'msg': message}
        return make_response(jsonify(result), 403)

    @staticmethod
    def not_found(message):
        result = {'error': 'not found', 'msg': message}
        return make_response(jsonify(result), 404)
