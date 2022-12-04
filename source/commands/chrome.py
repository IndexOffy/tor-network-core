from base.command import BaseCommand
from process import (
    chrome_explore_page,
    chrome_search_page
)


class CommandChrome(BaseCommand):
    """Command Chrome process
    """

    def explore_page(self):
        """python source/main.py chrome --run explore_page
        """
        chrome_explore_page()

    def search_page(self):
        """python source/main.py chrome --run search_page
        """
        chrome_search_page()
