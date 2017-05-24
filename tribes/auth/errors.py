# !-*- encoding=utf-8 -*-
"""
    auth.errors.py
    ~~~~~~~~~~~~~~~~~~

    服务单独的异常处理, 只在蓝图和Flask实例中生效，api扩展无效
    # example
    from auth import auth
    from common.errors import ErrorHandler

    @auth.error_handler(ValueError)
    def error_handler(e):
        return ErrorHandler.not_found(e.args[0])

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
