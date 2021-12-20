#!/usr/bin/env python
import os
import sys

try:
    # import MySQLdb  # noqa: F401, imported for side effect
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    import dmoj_install_pymysql  # noqa: F401, imported for side effect

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')

    from django.core.management import execute_from_command_line
    # noinspection PyUnresolvedReferences
    import django_2_2_pymysql_patch  # noqa: F401, imported for side effect

    execute_from_command_line(sys.argv)
