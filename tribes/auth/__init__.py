# !-*- encoding=utf-8 -*-
"""
Module Description

__init__.py create by v-zhidu
"""

from flask import Blueprint

app = Blueprint('auth', __name__)

from . import github_api
