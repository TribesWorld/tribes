# !-*- encoding=utf-8 -*-
"""
Module Description

__init__.py create by v-zhidu
"""
from flask import Blueprint
from common.service import api, db

auth = Blueprint('auth', __name__)

from auth import errors

from resources.user_resource import UserResource
api.add_resource(UserResource, '/user/<user_id>')
