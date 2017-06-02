# !-*- encoding=utf-8 -*-
"""
    dao.__init__.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from common.service import db
from common.database import Database
from flask import current_app

db_context = Database(db)


@db_context.before_connect
def before_connect():
    current_app.logger.debug('open')


@db_context.after_connect
def after_connect():
    current_app.logger.debug('close')


@db_context.before_transcation
def before_trans():
    current_app.logger.debug('open trans')


@db_context.after_transcation
def after_trans():
    current_app.logger.debug('close trans')


@db_context.across_error
def across_error(error):
    current_app.logger.debug(error.args[0])


@db_context.on_execute_sql
def on_execute_sql(sql):
    current_app.logger.debug(sql)
