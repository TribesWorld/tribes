# !-*- encoding=utf-8 -*-
"""
    tribes.tribes
    ~~~~~~~~~~~~~~~~~~

    应用程序的主入口，继承自common.service模块，主要作用是组装多个应用，并做一些全局上的配置

    :copyright: (c) YEAR by v-zhidu.
    :license: LICENSE_NAME, see LICENSE_FILE
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from common.service import Service
from auth.auth_service import AuthService


class Tribes(Service):
    """
    Tribes类

    用于创建Flask实例,主要作用是组合项目中的不同服务

    Public Attributes
         : instance Flask实例
    """

    def register_component(self, app, **kwargs):
        """覆盖common.service模块中的默认注册方法，组合项目中不同的服务
        """
        # 统一身份认证服务
        auth_service = AuthService(**kwargs).instance
        app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
            '/auth': auth_service
        })

        super(Tribes, self).register_component(app, **kwargs)


if __name__ == '__main__':
    application = Tribes(use_db=True)
    run_simple('localhost', 8000, application.instance,
               use_reloader=True, use_debugger=True, use_evalex=True)
