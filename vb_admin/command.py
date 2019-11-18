# pylint: disable=R0201

import argparse
import os
import shutil
import sys

from vb_admin import __version__ as VERSION

__all__ = ['execute_from_command_line']


class Command:
    def __init__(self):
        self.verbosity = 0
        self.cwd = os.getcwd()
        self.layout_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'layout'
        )
        self.target = self.cwd

    def out(self, *messages):
        sys.stdout.write(f'{" ".join(messages)}\n')

    def err(self, *messages):
        sys.stderr.write(f'{" ".join(messages)}\n')

    def set_target(self, target_path):
        if target_path == '.':
            return

        if not os.path.exists(target_path):
            self.err(f'Target path not found: {target_path}')
            sys.exit(1)

        self.target = target_path

    def execute(self):
        command_choices = ['startproject']

        parser = argparse.ArgumentParser(description='Create new Django project')
        parser.add_argument(
            'command',
            choices=command_choices,
            type=str,
            nargs='?',
            action='store',
            help='Name of command(s)',
        )
        parser.add_argument('-t', '--target', type=str, help='Target path', default='.')
        parser.add_argument(
            '-v',
            '--verbosity',
            type=int,
            choices=[0, 1],
            help='Verbose mode',
            default=0,
        )
        parser.add_argument('--version', action='version', version=VERSION)

        args = parser.parse_args()

        if args.command is None:
            parser.print_help()

        self.verbosity = args.verbosity
        self.set_target(args.target)

        if args.command == 'startproject':
            self.startproject()

    def startproject(self):
        if self.verbosity > 0:
            self.out(f'Copying files to: {self.target}')

        for item in os.listdir(self.layout_dir):
            source = os.path.join(self.layout_dir, item)
            destination = os.path.join(self.target, item)

            if os.path.isdir(source):
                if self.verbosity > 0:
                    self.out(f'Creating: {destination} folder')
                shutil.copytree(source, destination)
            else:
                if self.verbosity > 0:
                    self.out(f'Copying {destination}')
                shutil.copy2(source, destination)

        src_development_config_file = os.path.join(
            self.layout_dir, 'config', 'settings', 'development.example.py'
        )
        src_test_config_file = os.path.join(
            self.layout_dir, 'config', 'settings', 'test.example.py'
        )

        dst_development_config_file = os.path.join(
            self.target, 'config', 'settings', 'development.py'
        )
        dst_test_config_file = os.path.join(
            self.target, 'config', 'settings', 'test.py'
        )

        if self.verbosity > 0:
            self.out('Cloning: development.py')
        shutil.copy2(src_development_config_file, dst_development_config_file)

        if self.verbosity > 0:
            self.out('Cloning: test.py')
        shutil.copy2(src_test_config_file, dst_test_config_file)
        
        python_version_file = os.path.join(self.target, '.python-version')
        current_python_version = f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}' 
        
        with open(python_version_file, 'w') as filepointer:
            filepointer.write(current_python_version)

        if self.verbosity > 0:
            self.out(f'.python-version is set to {current_python_version}')
                
        if self.verbosity > 0:
            self.out(f'Copy completed')

        self.out('Setup completed...')
        self.out('Now, create your virtual environment and run')
        self.out('\n\tpip install -r requirements/development.pip\n')


def execute_from_command_line():
    command = Command()
    command.execute()
