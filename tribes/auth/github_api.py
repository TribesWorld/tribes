# !-*- encoding=utf-8 -*-
"""
身份认证模块

auth_test.py create by v-zhidu
"""

from flask import request, url_for, redirect
from auth import app

import requests
import requests.auth

CLIENT_ID = '0c3f470b984e0d972cd8'
CLIENT_SECRET = 'aaff61a7280b590b27c3ff9c1042f59d7912ae5a'
REDIRECT_URL = 'http://localhost:65010/git_call_back'


@app.route('/')
def home():
    """
    测试
    """
    text = '<a href="%s">Authenticate with github</a>'
    return text % make_authorization_url()


@app.route('/user')
def get_github_user():
    if not request.headers.get('Authorization'):
        return redirect(url_for('auth.index'))
    else:
        token = request.headers.get('Authorization')
        res = requests.get('https://api.github.com/user',
                           headers={'Authorization': token})

        return res.text


@app.route('/git_call_back')
def github_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        # Uh-oh, this request wasn't started by us!
        pass
    code = request.args.get('code')
    # We'll change this next line in just a moment
    token = get_access_token(code, state)
    return "got an access token! %s" % token


def make_authorization_url():
    """
    Get authorization address.
    """
    from uuid import uuid4
    state = str(uuid4())
    save_created_state(state)
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URL
    }
    import urllib
    url = 'https://github.com/login/oauth/authorize?' + \
        urllib.urlencode(params)

    return url


def get_access_token(code, state):
    # client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {'client_id': CLIENT_ID,
                 'client_secret': CLIENT_SECRET,
                 'code': code,
                 'state': state,
                 'redirect_uri': REDIRECT_URL}
    response = requests.post(
        "https://github.com/login/oauth/access_token", data=post_data, headers={'Accept': 'application/json'})
    token_json = response.json()
    return token_json["access_token"]


def save_created_state(state):
    """
    Left as an exercise to the reader.
    You may want to store valid states in a database or memcache,
    or perhaps cryptographically sign them and verify upon retrieval.
    """
    pass


def is_valid_state(state):
    return True
