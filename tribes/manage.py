#! /usr/bin/env python
"""
Module Description

manage.py create by v-zhidu
"""

from flask_script import Manager, Shell
from tribes import Tribes

tribes = Tribes()

manager = Manager(tribes.instance)

if __name__ == '__main__':
    manager.run()
