# !-*- encoding=utf-8 -*-
"""
Base Service

base_app.py create by v-zhidu
"""
from __future__ import unicode_literals

from abc import abstractmethod

from flask import Flask

import constant


class Service(object):
    """Abstract Service.
    """

    def __init__(self, **kwargs):
        self._instance = Flask(__name__)
        self._config_instance(self._instance, **kwargs)
        self.register_component(self._instance, **kwargs)

    def _config_instance(self, app, **kwargs):
        config_file = kwargs.get(
            'tribes_config', constant.TRIBES_DEFAULT_CONFIG)

        if config_file is not None:
            app.config.from_json(config_file, silent=False)

    @property
    def instance(self):
        """
        Flask Instance
        """
        return self._instance

    @abstractmethod
    def register_component(self, app, **kwargs):
        pass


if __name__ == '__main__':
    a = Service()
    a.instance.run()
