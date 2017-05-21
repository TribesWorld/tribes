# !-*- encoding=utf-8 -*-
"""
统一身份认证服务

auth_service.py create by v-zhidu
"""
from service import Service
from utils import initialize_class


class AuthService(Service):
    """统一身份认证服务
    """

    def register_component(self, app, **kwargs):
        """register component.
        """
        from demo import a as auth_blueprint
        self.instance.register_blueprint(auth_blueprint)


if __name__ == '__main__':
    application = AuthService()
    application.instance.run(debug=True)
