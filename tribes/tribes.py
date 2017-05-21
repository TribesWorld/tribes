# !-*- encoding=utf-8 -*-
"""
Application Entry

start_up.py create by v-zhidu
"""
import os
from config import DefaultConfig

from auth.auth_service import AuthService
from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware


class Tribes(object):
    """
    Tribes Object
    """

    def __init__(self, **kwargs):
        """
        Initialize a Falsk object.
        """
        self._tribes = self._initialize_tribes(**kwargs)

    def _initialize_tribes(self, **kwargs):
        """
        Create an instance of tribes.
        """
        config_file = kwargs.get('config_file', None)

        app = Flask(__name__)

        # load configuration
        app.config.from_object(DefaultConfig)
        if config_file is not None:
            app.config.from_json(config_file, silent=True)

        # register component
        self.register_component(app, **kwargs)

        return app

    def register_component(self, app, **kwargs):
        """
        Register route and error handler
        """
        # authentication service
        service1 = AuthService(**kwargs)
        app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
            '/auth': service1.instance
        })

    def start_tribes(self):
        """
        Fire application
        """
        run_simple('localhost', 5000, self._tribes,
                   use_reloader=True, use_debugger=True, use_evalex=True)
        self._tribes.run()


if __name__ == '__main__':
    application = Tribes(
        config_file='/Users/duzhiqiang/Code/tribes/tribes/_config/dev.json')
    application.start_tribes()
