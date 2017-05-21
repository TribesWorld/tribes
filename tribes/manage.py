#! /usr/bin/env python

import os
from flask_script import Manager, Shell
from tribes import Tribes
import constant

if not os.getenv('TRIBES_CONFIG'):
    tribes = Tribes(tribes_config='D:\\Code\\tribes\\tribes\\dev.json')
else:
    tribes = Tribes(tribes_config='D:\\Code\\tribes\\tribes\\dev.json')

manager = Manager(tribes.instance)

manager.add_command("shell", Shell)
if __name__ == '__main__':
    manager.run()
