# !-*- encoding=utf-8 -*-
"""
    services.__init__.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from api.user import user


def add_domain_errors(app):
    """添加业务逻辑异常处理"""
    # from common.errors import make_error

    # @app.errorhandler(404)
    # def method_not_found(e):
    #     """请求方法未找到"""
    #     return make_error(404, 'Ser1vice Not Found')
