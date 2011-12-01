#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    settings_local_path = 'berkerpeksag/settings_local.py'
    settings_name = 'berkerpeksag.settings'
    settings = settings_name + '_local' if os.path.exists(settings_local_path) else settings_name
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
