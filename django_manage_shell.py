# там где и manage.py файл
import os
from django.core import management
import sys


from runpy import run_module


def run(working_dir):
    sys.path.insert(0, working_dir)
    manage_file = os.getenv('PYCHARM_DJANGO_MANAGE_MODULE')
    if not manage_file:
        manage_file = 'manage'

    def execute_manager(settings_mod, argv=None):
        management.setup_environ(settings_mod)

    management.execute_manager = execute_manager

    def execute_from_command_line(argv=None):
        pass

    management.execute_from_command_line = execute_from_command_line

    run_module(manage_file, None, '__main__', True)


"""
in python console
from store.settings import BASE_DIR
Вместо store может быть другой проект
---

import sys, os; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
from store.settings import BASE_DIR
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run(BASE_DIR)
"""