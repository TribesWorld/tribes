# !-*- encoding=utf-8 -*-
"""
user 查询方法

user_dao.py create by v-zhidu
"""
from common.service import db


def is_user_existed(user_id):
    with db.engine.connect() as conn:
        result = conn.execute(
            'select count(1) from t_user where id={0}'.format(user_id))
        return result.fetchone()


def find_user_by_id(user_id):
    with db.engine.connect() as conn:
        result = conn.execute(
            'select * from t_user where id={0}'.format(user_id))
        return result.fetchone()
