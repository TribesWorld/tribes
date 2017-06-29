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
from config import configuration

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from common.authenticate import JWT
from common.errors import add_global_errors

db = SQLAlchemy()
jwt = JWT()
mail = Mail()


class App(object):
    """服务抽象类, Flask抽象工厂"""

    def __init__(self, **kwargs):
        self._instance = Flask(__name__)
        self._config_instance(self._instance, **kwargs)
        self.error_handler(self._instance)
        self.register_component(self._instance, **kwargs)

    def _config_instance(self, app, **kwargs):
        config_name = kwargs.get('config_name', 'default')
        app.config.from_object(configuration[config_name])

    @property
    def instance(self):
        """开放给外部访问Flask实例的权限"""
        return self._instance

    @abstractmethod
    def error_handler(self, app):
        """配置异常处理方法"""
        add_global_errors(app)

    @abstractmethod
    def register_component(self, app, **kwargs):
        """抽象方法，用于在Flask中注册蓝图和扩展"""

        # 选择是否开启JWT
        if kwargs.get('jwt', True) is True:
            app.logger.debug('loading JWT extension...')
            jwt.init_app(app)
        # 选择是否开启mail
        if kwargs.get('mail', True) is True:
            app.logger.debug('loading mail extension...')
            mail.init_app(app)
        # 加载数据库
        if kwargs.get('use_db', True) is True:
            app.logger.debug('loading database extension...')
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
