import os
import subprocess  # noqa: S404
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings.{0}'.format(os.environ.setdefault('DJANGO_ENV', 'production')),
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
os.environ.setdefault('CURRENT_GIT_TAG', CURRENT_GIT_TAG)
os.environ.setdefault('CURRENT_PYTHON_VERSION', CURRENT_PYTHON_VERSION)

application = get_wsgi_application()
