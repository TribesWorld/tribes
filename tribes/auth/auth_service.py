# !-*- encoding=utf-8 -*-
"""
统一身份认证服务

auth_service.py create by v-zhidu
"""

from tribes.base_service import BaseService
from tribes.utils import initialize_class


class AuthService(BaseService):
    """统一身份认证服务
    """

    def register_component(self, app, **kwargs):
        """register component.
        """
        demo = kwargs.get('demo', 'tribes.auth.demo')
        self._demo = initialize_class(demo, **kwargs)

        app.register_blueprint(self._demo)


if __name__ == '__main__':
    application = AuthService()
    application.service.run()
