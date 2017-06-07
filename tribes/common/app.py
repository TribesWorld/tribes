# !-*- encoding=utf-8 -*-
"""
    common.service.py
    ~~~~~~~~~~~~~~~~~~

    通用服务类，具有Flask工厂的作用，创建服务继承此类型后，具有一些全局的属性和方法

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""

from __future__ import unicode_literals

from abc import abstractmethod

from flask import Flask
from authenticate import JWT
from flask_sqlalchemy import SQLAlchemy

from config import configuration

db = SQLAlchemy()
jwt = JWT()


class App(object):
    """服务抽象类, Flask抽象工厂"""

    def __init__(self, **kwargs):
        self._instance = Flask(__name__)
        self._config_instance(self._instance, **kwargs)
        self.register_component(self._instance, **kwargs)
        self.error_handler(self._instance)

    def _config_instance(self, app, **kwargs):
        config_name = kwargs.get('config_name', 'default')
        app.config.from_object(configuration[config_name])

    @property
    def instance(self):
        """开放给外部访问Flask实例的权限"""
        return self._instance

    @abstractmethod
    def register_component(self, app, **kwargs):
        """抽象方法，用于在Flask中注册蓝图和扩展"""

        # 选择是否开启RESTApi
        if kwargs.get('oauth', True) is True:
            app.logger.info('loading JWT extension...')
            jwt.init_app(app)
        # 加载数据库
        if kwargs.get('use_db', False) is True:
            app.logger.info('loading database extension...')
            if 'SQLALCHEMY_DATABASE_URI' in app.config:
                db.init_app(app)
                db.app = app

            if 'SCRIPT_FOLDER' in app.config:
                from database import Database
                db_context = Database(db)
                db_context.init_db(app.config['SCRIPT_FOLDER'])
            else:
                raise Exception(
                    'SQLALCHEMY_DATABASE_URI must be set in config.py')

    def error_handler(self, app):
        """全局的异常处理方法"""
        from error_handler import make_error
        from common.exceptions import ValidationError
        from sqlalchemy.exc import OperationalError

        @app.errorhandler(ValidationError)
        def validation_error(e):
            """参数验证异常,返回400错误"""
            return make_error(400, message=e.args[0])

        @app.errorhandler(OperationalError)
        def database_error(e):
            """数据库操作异常"""
            return make_error(500, e.args[0])

        @app.errorhandler(405)
        def method_not_allowed(e):
            """请求方法错误"""
            return make_error(405, 'Method Not Allowed')
