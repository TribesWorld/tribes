# !-*- encoding=utf-8 -*-
"""
Module Description

__init__.py create by v-zhidu
"""


from flask import Blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import auth_test
