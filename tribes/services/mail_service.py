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

mail = Email(mail)
ADMIN_EMAIL = current_app.config.get('MAIL_DEFAULT_SENDER')


def send_verify_email(username, email, callback_url):
    """验证用户邮箱"""
    subject = 'Tribes - 用户验证邮件'
    mail.send_email(subject, ADMIN_EMAIL, [email], text_body=render_template(
        'verify_email.txt', name=username, verify_link=callback_url))
