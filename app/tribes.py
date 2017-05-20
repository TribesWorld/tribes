# !-*- encoding=utf-8 -*-
"""
Application Entry

start_up.py create by v-zhidu
"""
import os

from flask import Flask

from config import DefaultConfig


class Tribes(object):
    """
    Tribes Object
    """

    def __init__(self):
        """
        Initialize a Falsk object.
        """
        self._tribes = self._initialize_tribes()

    def _initialize_tribes(self, **kwargs):
        """
        Create an instance of tribes.
        """
        config_file = kwargs.get('config_file')

        app = Flask(__name__)

        # load configuration
        app.config.from_object(DefaultConfig)
        if config_file is not None:
            app.config.from_json(config_file, silent=True)

        # register component
        self.register_component(app)

        return app

    def register_component(self, app):
        """
        Register route and error handler
        """
        # authentication service
        from auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

    def start_tribes(self):
        """
        Fire application
        """
        self._tribes.run()


if __name__ == '__main__':
    application = Tribes()
    application.start_tribes()
