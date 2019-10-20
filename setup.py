import os

from setuptools import setup

CURRENT_WORKING_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_WORKING_DIRECTORY, 'README.md')) as fp:
    README = fp.read()

setup(
    name='django-vb-admin',
    version='1.0.11',
    description='Creates custom Django project.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/vbyazilim/django-vb-admin',
    author='vb YAZILIM',
    author_email='hello@vbyazilim.com',
    license='MIT',
    python_requires='>=3.0',
    packages=['vb_admin'],
    entry_points={'console_scripts': ['django-vb-admin=vb_admin:execute_from_command_line']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    include_package_data=True,
)
