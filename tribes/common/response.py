# !-*- encoding=utf-8 -*-
"""
    common.response.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import jsonify, make_response

from common.constant import CommonCodeConstants


def make_result(data):
    """构造返回值"""
    result = {'code': CommonCodeConstants.SUCCESS_CODE,
              'data': data}
    return make_response(jsonify(result))


def make_error(message, description=''):
    """创建视图方法的错误"""
    result = {'code': CommonCodeConstants.ERROR_CODE,
              'message': message, 'description': description}
    return make_response(jsonify(result))


def make_login_error(message, description=''):
    """创建视图方法的错误"""
    result = {'code': CommonCodeConstants.LOGIN_ERROR_CODE,
              'message': message, 'description': description}
    return make_response(jsonify(result), )
