from common.service import db
from common.database import Database

context = Database(db)


@context.before_connect
def before_connect():
    print 'open'


@context.after_connect
def after_connect():
    print 'close'


@context.across_error
def across_error(error):
    print error.args[0]
