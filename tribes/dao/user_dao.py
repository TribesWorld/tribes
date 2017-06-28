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


def is_email_existed(email):
    """检查email是否存在"""
    sql = "select count(*) from t_user where email='{0}'"

    return db_context.query_count(sql, email) == 1


def insert_user(account_name, password_hash, email, avatar):
    """添加用户"""
    sql = "insert into t_user (account_name, password_hash, email, avatar_url) \
        values ('{0}', '{1}', '{2}', '{3}')"
    get_id_sql = "select MAX(id) from t_user"

    db_context.execute(sql, account_name, password_hash, email, avatar)

    return db_context.query_count(get_id_sql)


def find_all():
    """根据用户id查找用户"""
    sql = 'select id, account_name, email, status from t_user'
    return db_context.query(sql)


def find_user_by_id(user_id):
    """根据用户id查找用户"""
    sql = 'select * from t_user where id={0}'
    return db_context.query_one(sql, user_id)


def find_user_by_login_name(account_name):
    """根据用户登录名称查找"""
    sql = "select * from t_user where account_name='{0}'"
    return db_context.query_one(sql, account_name)


def edit_user_name(user_id, account_name):
    """根据id修改用户姓名"""
    sql = "update t_user set account_name='{0}' where id={1}"
    return db_context.execute(sql, account_name, user_id)


def delete_user_by_id(user_id):
    """根据id删除用户"""
    sql = 'delete from t_user where id={0}'
    db_context.execute(sql, user_id)
