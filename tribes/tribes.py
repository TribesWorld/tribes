# !-*- encoding=utf-8 -*-
"""
Application Entry

start_up.py create by v-zhidu
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from auth import auth
from common.service import Service
from auth.auth_service import AuthService


class Tribes(Service):
    """
    Tribes Object
    """

    def register_component(self, app, **kwargs):
        """
        Register route and error handler
        """
        # authentication service
        auth_service = AuthService(**kwargs).instance
        app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
            '/auth': auth_service
        })


if __name__ == '__main__':
    application = Tribes(use_db=True)
    run_simple('localhost', 8000, application.instance,
               use_reloader=True, use_debugger=True, use_evalex=True)
