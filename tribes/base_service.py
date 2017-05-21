# !-*- encoding=utf-8 -*-
"""
Base Service

base_app.py create by v-zhidu
"""

from abc import abstractmethod

from flask import Flask


class BaseService(object):
    """Abstract Service.
    """

    def __init__(self, **kwargs):
        self._service = Flask(__name__)
        self._config_service(self._service, **kwargs)
        self.register_component(self._service, **kwargs)

    def _config_service(self, app, **kwargs):
        config_file = kwargs.get('config_file')

        if config_file is not None:
            app.config.from_json(config_file, silent=True)

    @property
    def service(self):
        return self._service

    @abstractmethod
    def register_component(self, app, **kwargs):
        pass
