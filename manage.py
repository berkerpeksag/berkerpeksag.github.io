#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings_local_path = 'berkerpeksag/settings_local.py'
    settings_prod_path = 'berkerpeksag/settings_prod.py'
    settings_name = 'berkerpeksag.settings'
    is_settings_local_exists = os.path.exists(settings_local_path)
    if os.path.exists(settings_local_path):
        settings = settings_name + '_local'
    elif os.path.exists(settings_prod_path):
        settings = settings_name + '_prod'
    else:
        settings = settings_name
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
