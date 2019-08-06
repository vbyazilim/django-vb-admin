import argparse

__all__ = ['execute_from_command_line']


class Command:
    def __init__(self):
        self.verbosity = 0

    def execute(self):
        command_choices = ['startproject']

        parser = argparse.ArgumentParser(description='Create new Django project')
        parser.add_argument(
            'command', choices=command_choices, type=str, nargs='?', action='store', help='Name of command(s)'
        )
        parser.add_argument('-v', '--verbosity', type=int, choices=[0, 1], help='Verbose mode', default=0)

        args = parser.parse_args()

        if args.command is None:
            parser.print_help()

        self.verbosity = args.verbosity

        if args.command == 'startproject':
            self.startproject()

    def startproject(self):
        pass


def execute_from_command_line():
    command = Command()
    command.execute()
