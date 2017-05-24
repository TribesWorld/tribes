#! /usr/bin/env python
# !-*- encoding=utf-8 -*-
"""
    tribes.manage.py
    ~~~~~~~~~~~~~~~~~~

    使用flask-script插件在命令行运行程序

    : copyright: (c) YEAR by v-zhidu.
    : license: LICENSE_NAME, see LICENSE_FILE
"""

from flask_script import Manager
from tribes import Tribes

tribes = Tribes(use_db=True)

manager = Manager(tribes.instance)

if __name__ == '__main__':
    manager.run()
