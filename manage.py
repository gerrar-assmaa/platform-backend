#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.popen("cmd.exe /c chcp 1252")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platform_backend.settings')
    
    #added to always run on default port of 8080
    import django
    django.setup()

    # Override default port for `runserver` command
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "8080"

    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
