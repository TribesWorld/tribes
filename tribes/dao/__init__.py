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

db_context = Database(db)


@db_context.before_connect
def before_connect():
    print 'open'


@db_context.after_connect
def after_connect():
    print 'close'


@db_context.across_error
def across_error(error):
    print error.args[0]
