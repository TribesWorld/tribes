# !-*- encoding=utf-8 -*-
"""
测试用例

demo.py create by v-zhidu
"""
from flask import Blueprint, current_app

a = Blueprint('a', __name__)


@a.route('/')
def index():
    """ demo
    """
    return current_app.config.get('MY_VALUE')
