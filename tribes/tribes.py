# !-*- encoding=utf-8 -*-
"""
Application Entry

start_up.py create by v-zhidu
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from auth.auth_service import AuthService
from common.service import Service


class Tribes(Service):
    """
    Tribes Object
    """

    def register_component(self, app, **kwargs):
        """
        Register route and error handler
        """
        # authentication service
        service1 = AuthService(**kwargs)
        app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
            '/auth': service1.instance
        })


if __name__ == '__main__':
    import os
    application = Tribes()
    run_simple('localhost', 5001, application.instance,
               use_reloader=True, use_debugger=True, use_evalex=True)
