import os
import subprocess  # noqa: S404
import sys

from django import VERSION
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'config.settings.{0}'.format(os.environ.setdefault('DJANGO_ENV', 'production'))
)

GIT_EXECUTE = subprocess.Popen(  # noqa: S603,S607
    ['git', 'describe', '--tag'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
)
GIT_OUTPUT, __ = GIT_EXECUTE.communicate()
CURRENT_GIT_TAG = str(GIT_OUTPUT, 'utf-8').strip() or 'N/A'

CURRENT_PYTHON_VERSION = (
    f'{sys.version_info.major}.'
    f'{sys.version_info.minor}.'
    f'{sys.version_info.micro}-'
    f'{sys.version_info.releaselevel}'
)

DJANGO_MAJOR_VERSION, DJANGO_MINOR_VERSION, DJANGO_PATCH_VERSION, DJANGO_VERSION_TAG, __ = VERSION
CURRENT_DJANGO_VERSION = (
    f'{DJANGO_MAJOR_VERSION}.' f'{DJANGO_MINOR_VERSION}.' f'{DJANGO_PATCH_VERSION}-' f'{DJANGO_VERSION_TAG}'
)

os.environ.setdefault('CURRENT_GIT_TAG', CURRENT_GIT_TAG)
os.environ.setdefault('CURRENT_PYTHON_VERSION', CURRENT_PYTHON_VERSION)
os.environ.setdefault('CURRENT_DJANGO_VERSION', CURRENT_DJANGO_VERSION)

application = get_wsgi_application()
