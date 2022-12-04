from base.command import BaseCommand
from base.api import RequestUrls, RequestLinks
from process import (
    chrome_explore_page,
    chrome_search_duckduckgo_page,
    chrome_search_google_page
)


class CommandChrome(BaseCommand):
    """Command Chrome process
    """

    def explore_page(self):
        """python source/main.py chrome

        --run explore_page
        --limit 5
        """
        request = RequestUrls()
        response = request.make_get(
            params=dict(
                verify=self.verify,
                fail=self.fail,
                running=self.running,
                limit=self.limit,
                order_by='asc'
            )
        )

        if response.status_code == 200:
            chrome_explore_page(data=response.json())

    def search_duckduckgo_page(self):
        """python source/main.py chrome

        --run search_duckduckgo_page
        --search 'duckduckgo'
        --page 1
        """
        chrome_search_duckduckgo_page(
            search=self.search,
            page=self.page
        )


    def search_google_page(self):
        """python source/main.py chrome

        --run search_google_page
        --search 'google'
        --page 1
        """
        chrome_search_google_page(
            search=self.search,
            page=self.page
        )
