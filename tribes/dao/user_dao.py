# !-*- encoding=utf-8 -*-
"""
    User实体的查询方法
    ~~~~~~~~~~~~~~~~~~

    包含UserResource所有的查询语句

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from common.service import db


def is_user_existed(user_id):
    """检查用户id是否存在"""
    with db.engine.connect() as conn:
        result = conn.execute(
            'select count(1) from t_user where id={0}'.format(user_id))
        return result.fetchone()[0] == 1


def find_user_by_id(user_id):
    """根据用户id查找用户"""
    with db.engine.connect() as conn:
        result = conn.execute(
            'select * from t_user where id={0}'.format(user_id))
        return result.fetchone()


def edit_user_name(user_id, name):
    """根据id修改用户姓名"""
    with db.engine.connect() as conn:
        result = conn.execute(
            "update t_user set name='{0}' where id={1}".format(name, user_id))
