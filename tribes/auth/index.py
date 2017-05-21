# !-*- encoding=utf-8 -*-
"""
测试用例

demo.py create by v-zhidu
"""
from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    """ index
    """
    return "index page"
