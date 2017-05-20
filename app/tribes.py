# !-*- encoding=utf-8 -*-
"""
Application Entry

start_up.py create by v-zhidu
"""
from flask import Flask


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
        config = kwargs.get('config', None)

        app = Flask(__name__)
        if config is not None:
            app.config.from_json(config)

        self.register_component(app)

        return app

    def register_component(self, app):
        """
        Register route and error handler
        """
        from auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

    def start_tribes(self, **kwargs):
        """
        Fire application
        """
        self._tribes.run(**kwargs)


if __name__ == '__main__':
    application = Tribes()
    application.start_tribes(debug=True, port=3579)
