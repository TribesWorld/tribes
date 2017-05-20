from . import auth


@auth.route('/')
def hello():
    return 'hello'
