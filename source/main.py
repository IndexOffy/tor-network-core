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
    options = dict(type=int, default=0)

    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    cmd_tor = subparsers.add_parser('tor')
    cmd_tor.add_argument(cmd_arg, required=True)
    cmd_tor.add_argument('--search', type=str)
    cmd_tor.add_argument('--verify', **options)
    cmd_tor.add_argument('--fail', **options)
    cmd_tor.add_argument('--running', **options)
    cmd_tor.add_argument('--page', type=int, default=1)
    cmd_tor.add_argument('--limit', type=int, default=100)
    cmd_tor.add_argument('--headless', type=int, default=1)
    cmd_tor.set_defaults(exec=CommandTor)

    cmd_chrome = subparsers.add_parser('chrome')
    cmd_chrome.add_argument(cmd_arg, required=True)
    cmd_chrome.add_argument('--search', type=str)
    cmd_chrome.add_argument('--verify', **options)
    cmd_chrome.add_argument('--fail', **options)
    cmd_chrome.add_argument('--running', **options)
    cmd_chrome.add_argument('--page', type=int, default=1)
    cmd_chrome.add_argument('--limit', type=int, default=100)
    cmd_chrome.add_argument('--headless', type=int, default=1)
    cmd_chrome.set_defaults(exec=CommandChrome)

    arguments = parser.parse_args()
    arguments.exec(**arguments.__dict__)


if __name__ == '__main__':
    main()
