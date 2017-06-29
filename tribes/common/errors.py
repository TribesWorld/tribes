# !-*- encoding=utf-8 -*-
"""
    common.errors.py
    ~~~~~~~~~~~~~~~~~~

    封装常用的异常处理操作

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from common.response import make_error


def add_global_errors(app):
    """全局异常处理"""
    from sqlalchemy.exc import SQLAlchemyError

    @app.errorhandler(SQLAlchemyError)
    def database_error(e):
        """数据库操作异常"""
        return make_error(message=e.args[0])

    @app.errorhandler(405)
    def method_not_allowed(e):
        """请求方法错误"""
        return make_error('Method Not Allowed')

    @app.errorhandler(404)
    def method_not_found(e):
        """请求方法未找到"""
        return make_error('Service Not Found')

    @app.errorhandler(500)
    def internal_server_error(e):
        """请求方法错误"""
        return make_error(message=e.args[0])
