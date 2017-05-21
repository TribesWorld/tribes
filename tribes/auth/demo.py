# !-*- encoding=utf-8 -*-
"""
测试用例

demo.py create by v-zhidu
"""

from flask import Blueprint
demo = Blueprint('demo', __name__, url_prefix='/demo')


@demo.route('/')
def index():
    """ demo
    """
    return 'auth.demo'
