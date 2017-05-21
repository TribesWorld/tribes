# !-*- encoding=utf-8 -*-
"""
测试用例

demo.py create by v-zhidu
"""

from auth import app


@app.route('/help')
def index():
    """ help page
    """
    return "This is a help page"
