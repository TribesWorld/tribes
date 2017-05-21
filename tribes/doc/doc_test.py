# !-*- encoding=utf-8 -*-
"""
文档管理模块

doc_test.py create by v-zhidu
"""

from . import doc


@doc.route('/')
def get_doc():
    return 'doc'
