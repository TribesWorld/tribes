# !-*- encoding=utf-8 -*-
"""
统一身份认证服务

auth_service.py create by v-zhidu
"""

from common.service import Service, db


class AuthService(Service):
    """统一身份认证服务
    """

    def __init__(self, **kwargs):
        super(AuthService, self).__init__(**kwargs)

    def register_component(self, app, **kwargs):
        """register component.
        """
        from auth import oauth
        oauth.init_app(app)
        # blueprint
        from auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        super(AuthService, self).register_component(app, **kwargs)


if __name__ == '__main__':
    application = AuthService()
    # from model import User, Client, Grant, Token
    db.create_all()
    application.instance.run(debug=True, port=5002)
