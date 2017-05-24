# !-*- encoding=utf-8 -*-
"""
    common.error_handler.py
    ~~~~~~~~~~~~~~~~~~

    封装常用的异常处理操作

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import make_response, jsonify


class ErrorHandler(object):
    """覆盖Http协议中的的错误信息"""

    @staticmethod
    def bad_request(message):
        """400错误，非法的请求，一般在参数异常时使用"""
        result = {'error': 'bad request', 'msg': message}
        return make_response(jsonify(result), 400)

    @staticmethod
    def unauthorized(message):
        """401错误，未授权的请求，一般在请求未被验证的情况下使用"""
        result = {'error': 'unauthorized', 'msg': message}
        return make_response(jsonify(result), 401)

    @staticmethod
    def forbidden(message):
        """403错误，禁止访问"""
        result = {'error': 'forbidden', 'msg': message}
        return make_response(jsonify(result), 403)

    @staticmethod
    def not_found(message):
        """404错误，未找到资源，一般在路由不正确以及资源找不到时使用"""
        result = {'error': 'not found', 'msg': message}
        return make_response(jsonify(result), 404)
