#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'config.settings.{0}'.format(os.environ.setdefault('DJANGO_ENV', 'development'))
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django  # noqa: F401 # pylint: disable=W0611
        except ImportError:
            raise ImportError(
                'Couldn\'t import Django. Are you sure it\'s installed and '
                'available on your PYTHONPATH environment variable? Did you '
                'forget to activate a virtual environment?'
            )
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
