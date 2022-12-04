from base.command import BaseCommand
from process import (
    tor_search_page,
    tor_search_relationship,
    tor_search_subpage
)


class CommandTor(BaseCommand):
    """Command Tor process
    """

    def search_page(self):
        """python source/main.py tor --run search_page
        """
        tor_search_page()

    def search_relationship(self):
        """python source/main.py tor --run search_relationship
        """
        tor_search_relationship()

    def search_subpage(self):
        """python source/main.py tor --run search_subpage
        """
        tor_search_subpage()
