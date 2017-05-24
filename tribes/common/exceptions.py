# !-*- encoding=utf-8 -*-
"""
    common.exceptions.py
    ~~~~~~~~~~~~~~~~~~

    应用程序中的异常，如需扩展请放到此模块下

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""


class ValidationError(ValueError):
    """参数校验错误，验证请求或参数格式不正确"""
    pass


class UserNotFoundError(Exception):
    """用户不存在异常"""
    pass
