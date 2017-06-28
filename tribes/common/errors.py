# !-*- encoding=utf-8 -*-
"""
    common.errors.py
    ~~~~~~~~~~~~~~~~~~

    封装常用的异常处理操作

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""


def make_error(staue_code, message, description=''):
    """创建视图方法的错误"""
    from flask import make_response, jsonify

    result = {'message': message, 'description': description}
    return make_response(jsonify(result), staue_code)


def add_global_errors(app):
    """全局异常处理"""
    from common.exceptions import ValidationError
    from sqlalchemy.exc import OperationalError

    @app.errorhandler(ValidationError)
    def validation_error(e):
        """参数验证异常,返回400错误"""
        return make_error(400, message=e.args[0])

    @app.errorhandler(OperationalError)
    def database_error(e):
        """数据库操作异常"""
        return make_error(500, e.args[0])

    @app.errorhandler(405)
    def method_not_allowed(e):
        """请求方法错误"""
        return make_error(405, 'Method Not Allowed')

    @app.errorhandler(404)
    def method_not_found(e):
        """请求方法未找到"""
        return make_error(404, 'Service Not Found')
