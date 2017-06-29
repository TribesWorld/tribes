# !-*- encoding=utf-8 -*-
"""
    common.exceptions.py
    ~~~~~~~~~~~~~~~~~~

    应用程序中的异常，如需扩展请放到此模块下

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""


class TribesError(Exception):
    """应用程序业务逻辑异常"""

    def __init__(self, message):
        self.message = message
        super(TribesError, self).__init__()


class ValidationError(TribesError):
    """参数校验错误，验证请求或参数格式不正确"""

    def __init__(self, varible):
        super(ValidationError, self).__init__(str(varible) + ' is invalid')


class UserNotFoundError(TribesError):
    """用户不存在异常"""

    def __init__(self, name_or_id):
        super(UserNotFoundError, self).__init__(
            'user id or name: ' + str(name_or_id) + ' is not exist.')


class UserEmailExistError(TribesError):
    """用户名已存在异常"""

    def __init__(self, email):
        super(UserEmailExistError, self).__init__(
            str(email) + ' is already exist.')
