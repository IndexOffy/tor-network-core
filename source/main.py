"""
Initial Module
"""


from argparse import ArgumentParser

from commands.chrome import CommandChrome
from commands.tor import CommandTor


def main():
    """Project base function to orchestrate the execution
    commands of data scraping processes.
    """
    cmd_arg = '--run'

    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    cmd_tor = subparsers.add_parser('tor')
    cmd_tor.add_argument(cmd_arg, required=True)
    cmd_tor.set_defaults(exec=CommandTor)

    cmd_chrome = subparsers.add_parser('chrome')
    cmd_chrome.add_argument(cmd_arg, required=True)
    cmd_chrome.set_defaults(exec=CommandChrome)

    arguments = parser.parse_args()
    arguments.exec(run=arguments.run)


if __name__ == '__main__':
    main()
