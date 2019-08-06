import sys

__all__ = ['execute_from_command_line']


class Command:
    def __init__(self, argv):
        self.argv = argv or sys.argv[:]

    def execute(self):
        print('self.argv', self.argv)


def execute_from_command_line(argv=None):
    utility = Command(argv)
    utility.execute()
