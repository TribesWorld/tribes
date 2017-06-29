# !-*- encoding=utf-8 -*-
"""
    services.mail_service.py
    ~~~~~~~~~~~~~~~~~~

    邮件服务

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask import render_template, current_app
from common.app import mail
from common.emails import Email
from common.utils import generate_token

mail = Email(mail)


def send_verify_email(username, email, callback_url, host):
    """验证用户邮箱"""
    subject = 'Tribes - 用户验证邮件'
    data = {'name': username, 'email': email, 'callback_url': callback_url}
    token = generate_token(data, current_app.config['SECRET_KEY'])
    active_accout_url = 'http://{0}/api/auth/active_account?token={1}'.format(
        host, token)

    mail.send_email(subject, [email], text_body=render_template(
        'verify_email.txt', name=username, verify_link=active_accout_url))
