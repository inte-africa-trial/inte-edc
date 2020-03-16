#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management import color_style

style = color_style()


def main():
    default = "inte_edc.settings.defaults"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inte_edc.settings.defaults")
    if os.environ.get("DJANGO_SETTINGS_MODULE") == default:
        sys.stderr.write(
            style.ERROR(
                f"DJANGO_SETTINGS_MODULE not set. Using `{default}`. "
                f"Assuming a test environment (manage.py).\n"
            )
        )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
