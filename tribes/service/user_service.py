# !-*- encoding=utf-8 -*-
"""
    service.user_service.py
    ~~~~~~~~~~~~~~~~~~

    A brief description goes here.

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from dao import user_dao, db_context
from common.database import database


@database(db_context, False)
def find_all_user():
    """查找所有用户"""
    return user_dao.find_all()


def find_user_by_id(id):
    """根据id查找用户"""
    if not isinstance(id, int) or id < 0:
        raise ValueError('user id not exist.')
