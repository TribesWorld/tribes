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
        # 覆盖原始的数据库地址
        if 'AUTH_DATABASE_URI' in app.config:
            app.config['SQLALCHEMY_DATABASE_URI'] = app.config['AUTH_DATABASE_URI']
        # 注册蓝图
        from auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        super(AuthService, self).register_component(app, **kwargs)
