# !-*- encoding=utf-8 -*-
"""
Module Description

__init__.py create by v-zhidu
"""

from flask import Blueprint, current_app

auth = Blueprint('auth', __name__)
from flask_oauthlib.provider import OAuth2Provider

oauth = OAuth2Provider()

from . import github_api
from . import oauth_service
