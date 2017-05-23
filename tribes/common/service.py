# !-*- encoding=utf-8 -*-
"""
Base Service

base_app.py create by v-zhidu
"""
from __future__ import unicode_literals

from abc import abstractmethod
from config import config

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()


class Service(object):
    """Abstract Service.
    """

    def __init__(self, **kwargs):
        self._instance = Flask(__name__)
        self._config_instance(self._instance, **kwargs)
        self.register_component(self._instance, **kwargs)
        self.error_handler(self._instance, **kwargs)

    def _config_instance(self, app, **kwargs):
        config_name = kwargs.get('config_name', 'default')
        app.config.from_object(config[config_name])

    @property
    def instance(self):
        """
        Flask Instance
        """
        return self._instance

    @abstractmethod
    def register_component(self, app, **kwargs):
        """ 加载组件
        """
        api.init_app(app)
        # 加载数据库
        if 'SQLALCHEMY_DATABASE_URI' in app.config:
            db.init_app(app)
            db.app = app

    def error_handler(self, app, **kwargs):
        from error_handler import ErrorHandler
        from exceptions import ValidationError

        @app.errorhandler(ValidationError)
        def validation_error(e):
            """
            参数验证异常
            """
            return ErrorHandler.bad_request(e.args[0])
