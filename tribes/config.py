# !-*- encoding=utf-8 -*-
"""
    tribes.config.py
    ~~~~~~~~~~~~~~~~~~

    应用程序配置模块，包含开发和生产不同环境的配置

    : copyright: (c) 2017 by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """默认配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = True

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # 如需拆分数据库，则添加此配置项
    AUTH_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


configuration = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
