from werkzeug import security
from flask_oauthlib.client import OAuth
from flask import session, Flask, url_for, request, jsonify

app = Flask(__name__)

oauth = OAuth()
github = oauth.remote_app('github', base_url='http://github.com/login',
                          authorize_url='http://github.com/login/oauth/authorize', access_token_url='https://github.com/login/oauth/access_token', app_key='GITHUB')
app.config['GITHUB'] = {'consumer_key': '0c3f470b984e0d972cd8',
                        'consumer_secret': 'aaff61a7280b590b27c3ff9c1042f59d7912ae5a'}
app.config['SECRET_KEY'] = '0c3f470b984e0d972cd8'

oauth.init_app(app)


def change_github_header(uri, headers, body):
    auth = headers.get('Authorization')
    if auth:
        auth = auth.replace('Bearer', 'token')
        headers['Authorization'] = auth
    return uri, headers, body


# github.pre_request = change_github_header


@app.route('/github/user')
def get_user():
    response = github.get('https://api.github.com/user')
    return jsonify(response.data)


@github.tokengetter
def get_github_token(token=None):
    return session.get('github_token')


@app.route('/login')
def login():
    return github.authorize(callback='http://localhost:65010/authorized')


@app.route('/authorized')
def authorized():
    resp = github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['github_token'] = (resp['access_token'], '')
    return jsonify(oauth_token=resp['access_token'])


if __name__ == '__main__':
    import os
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    app.run(debug=True, port=65010)
