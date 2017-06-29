# !-*- encoding=utf-8 -*-
"""
    services.__init__.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from api.user import user
from api.auth import auth


def add_domain_errors(app):
    """添加业务逻辑异常处理"""
    from common.response import make_error
    from service.exceptions import TribesError

    @app.errorhandler(TribesError)
    def tribes_error(e):
        """业务逻辑异常"""
        return make_error(e.message)
