# !-*- encoding=utf-8 -*-
"""
    common.exceptions.py
    ~~~~~~~~~~~~~~~~~~

    应用程序中的异常，如需扩展请放到此模块下

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""


class ValidationError(ValueError):
    """参数校验错误，验证请求或参数格式不正确"""
    pass


class UserNotFoundError(Exception):
    """用户不存在异常"""
    pass


def add_domain_errors(app):
    """添加业务逻辑异常处理"""

    from common.errors import make_error

    @app.errorhandler(404)
    def method_not_found(e):
        """请求方法未找到"""
        return make_error(404, 'Service Not Found')
