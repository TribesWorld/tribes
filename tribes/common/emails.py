# !-*- encoding=utf-8 -*-
"""
    common.emails.py
    ~~~~~~~~~~~~~~~~~~

    邮件服务

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""
from flask_mail import Message
from decorators import async


class Email(object):
    """Email 服务"""

    def __init__(self, mail):
        self._mail = mail

    # TODO(du_zhi_qiang@163.com): 异步发送邮件
    def send_async_email(self, msg):
        """异步发送邮件"""
        self._mail.send(msg)

    def send_email(self, subject, sender, recipients, text_body=None, html_body=None):
        """发送邮件"""
        msg = Message(subject, sender=sender, recipients=recipients)

        if text_body:
            msg.body = text_body
        if html_body:
            msg.html = html_body

        self.send_async_email(msg)
