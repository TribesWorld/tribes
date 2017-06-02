# !-*- encoding=utf-8 -*-
"""
    common.error_handler.py
    ~~~~~~~~~~~~~~~~~~

    封装常用的异常处理操作

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import make_response, jsonify
from flask_restful import abort


def make_error(staue_code, message, description=''):
    """创建视图方法的错误"""
    result = {'message': message, 'description': description}
    return make_response(jsonify(result), staue_code)


def make_api_error(staue_code, description):
    """创建api方法的错误"""
    result = {'description': description, 'message': ''}
    abort(staue_code, **result)
