#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    dev_settings = {
        "true": "monian.dev_settings",
        "false": "monian.settings"
    }
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        dev_settings[os.environ.get("DJANGO_DEV", "false")])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
