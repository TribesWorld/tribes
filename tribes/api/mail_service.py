# !-*- encoding=utf-8 -*-
"""
    services.mail_service.py
    ~~~~~~~~~~~~~~~~~~

    邮件服务

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import current_app, render_template

from common.app import mail
from common.emails import Email
from common.utils import encrypt
mail = Email(mail)

ADMIN_EMAIL = current_app.config.get('MAIL_DEFAULT_SENDER')
SECRET_KEY = current_app.config.get('SECRET_KEY')


def send_verify_email(username, email, callback_url):
    """验证用户邮箱"""
    subject = 'Tribes - 用户验证邮件'
    active_accout_url = 'http://localhost:5001/api/active_account/' + \
        encrypt(SECRET_KEY, SECRET_KEY, email)
    mail.send_email(subject, ADMIN_EMAIL, [email], text_body=render_template(
        'verify_email.txt', name=username, verify_link=active_accout_url))
