# !-*- encoding=utf-8 -*-
"""
统一身份认证服务

auth_service.py create by v-zhidu
"""
from service import Service


class AuthService(Service):
    """统一身份认证服务
    """

    def __init__(self, **kwargs):
        super(AuthService, self).__init__(**kwargs)

    def register_component(self, app, **kwargs):
        """register component.
        """
        from . import auth as auth_blueprint
        self.instance.register_blueprint(auth_blueprint)


if __name__ == '__main__':
    application = AuthService(config_file='D:\\Code\\tribes\\tribes\\dev.json')
    application.instance.run(debug=True)
