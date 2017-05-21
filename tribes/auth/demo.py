# !-*- encoding=utf-8 -*-
"""
测试用例

demo.py create by v-zhidu
"""
from . import auth


@auth.route('/')
def index():
    """ demo
    """
    return "d"
