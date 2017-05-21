# !-*- encoding=utf-8 -*-
"""
Base Service

base_app.py create by v-zhidu
"""

from abc import abstractmethod

from flask import Flask


class Service(object):
    """Abstract Service.
    """

    def __init__(self, **kwargs):
        self._instance = Flask(__name__)
        self._config_instance(self._instance, **kwargs)
        self.register_component(self._instance, **kwargs)

    def _config_instance(self, app, **kwargs):
        config_file = kwargs.get('config_file')

        if config_file is not None:
            app.config.from_json(config_file, silent=True)

    @property
    def instance(self):
        return self._instance

    @abstractmethod
    def register_component(self, app, **kwargs):
        pass


if __name__ == '__main__':
    a = Service()
    a.instance.run()
