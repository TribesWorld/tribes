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
from service.exceptions import ValidationError, UserNotFoundError


@database(db_context, False)
def find_all_user():
    """查找所有用户"""
    return user_dao.find_all()


@database(db_context, False)
def find_user_by_id(user_id):
    """根据id查找用户"""
    if not isinstance(user_id, int) or user_id < 0:
        raise ValidationError('user_id')

    user = user_dao.find_user_by_id(user_id)

    if not user:
        raise UserNotFoundError(user_id)

    return user


@database(db_context, False)
def find_user_by_login_name(user_name):
    """根据用户名查找用户"""
    user = user_dao.find_user_by_login_name(user_name)

    if not user:
        raise UserNotFoundError(user_name)

    return user


@database(db_context, True)
def add_user(email, user_name, password):
    """添加新用户"""
    from service.mail_service import send_verify_email
    from service.exceptions import UserEmailExistError
    from common.utils import generate_avatar, encode_password

    if user_dao.is_email_existed(email):
        raise UserEmailExistError(email)

    # 生成默认头像
    avartar_url = generate_avatar()
    # 持久化用户
    user_id = user_dao.insert_user(user_name, encode_password(
        password), email, avartar_url)
    # TODO(du_zhi_qiang@163.com): 异步发送确认邮件
    send_verify_email(user_name, email, 'temp_url')

    return user_id


@database(db_context, True)
def update_user_name(user_id, user_name):
    """更新用户登录名称"""
    if not user_dao.is_user_existed(user_id):
        raise UserNotFoundError(user_id)

    user_dao.edit_user_name(user_id, user_name)

    return True


@database(db_context, True)
def delete_user(user_id):
    """更新用户登录名称"""
    if not user_dao.is_user_existed(user_id):
        raise UserNotFoundError(user_id)

    user_dao.delete_user_by_id(user_id)

    return True


@database(db_context, False)
def check_email(email):
    """检查邮箱是否存在"""
    return not user_dao.is_email_existed(email)
