# !-*- encoding=utf-8 -*-
"""
    User实体的查询方法
    ~~~~~~~~~~~~~~~~~~

    包含UserResource所有的查询语句

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from dao import db_context


def is_user_existed(user_id):
    """检查用户id是否存在"""
    sql = 'select count(*) from t_user where id={0}'

    return db_context.query_count(sql, user_id) == 1


def insert_user(name):
    """添加用户"""
    sql = "insert into t_user (name) values ('{0}')"

    print db_context.execute(sql, name)
    return db_context.execute(sql, name)


def find_all():
    """根据用户id查找用户"""
    sql = 'select * from t_user'
    return db_context.query(sql)


def find_user_by_id(user_id):
    """根据用户id查找用户"""
    sql = 'select * from t_user where id={0}'
    return db_context.query_one(sql, user_id)


def edit_user_name(user_id, name):
    """根据id修改用户姓名"""
    sql = "update t_user set name='{0}' where id={1}"
    return db_context.execute(sql, name, user_id)


def delete_user_by_id(user_id):
    """根据id删除用户"""
    sql = 'delete from t_user where id={0}'
    db_context.execute(sql, user_id)
