# !-*- encoding=utf-8 -*-
"""
    auth.__init__.py
    ~~~~~~~~~~~~~~~~~~

    服务中资源和错误的配置

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import Blueprint
from common.service import api, db

# 初始化蓝图
auth = Blueprint('auth', __name__)

# 导入视图的异常

# # 导入RESTAPI资源
from resources.user_resource import UserResource
