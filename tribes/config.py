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
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is a key123'
    SSL_DISABLE = True

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SCRIPT_FOLDER = os.environ.get('SCRIPT_FOLDER')
    # 如需拆分数据库，则添加此配置项
    # AUTH_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    # 邮件服务配置
    MAIL_SERVER = 'smtp.163.com'
    # MAIL_PORT: default 25
    # MAIL_USE_TLS: default False
    # MAIL_USE_SSL: default False
    # MAIL_DEBUG: default app.debug
    MAIL_USERNAME = 'du_zhi_qiang@163.com'
    MAIL_PASSWORD = 'DU5573574'
    MAIL_DEFAULT_SENDER = 'du_zhi_qiang@163.com'
    # MAIL_MAX_EMAILS: default None
    # MAIL_SUPPRESS_SEND: default app.testing
    # MAIL_ASCII_ATTACHMENTS: default False


configuration = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
