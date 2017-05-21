#! /usr/bin/env python

import os
from flask_script import Manager, Shell
from tribes import Tribes
import constant

tribes = Tribes()

manager = Manager(tribes.instance)

manager.add_command("shell", Shell)
if __name__ == '__main__':
    manager.run()
