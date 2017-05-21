# !-*- encoding=utf-8 -*-
"""Module Description

__init__.py create by v-zhidu
"""


from flask import Blueprint

doc = Blueprint('doc', __name__, url_prefix='/doc')

from . import doc_test
