# !-*- encoding=utf-8 -*-
""" 应用程序配置

config.py create by v-zhidu
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ 默认配置
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = True

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    """ 开发环境配置
    """
    DEBUG = True
    # OAUTH2_PROVIDER_TOKEN_EXPIRES_IN = 3600
    # OAUTH2_PROVIDER_ERROR_URI = '/oauth/errors'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
