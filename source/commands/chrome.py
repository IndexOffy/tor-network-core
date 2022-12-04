"""
Chrome Commands Module
"""


from base.api import RequestUrls
from base.command import BaseCommand
from process import (
    chrome_explore_page,
    chrome_search_duckduckgo_page,
    chrome_search_google_page
)


class CommandChrome(BaseCommand):
    """Command Chrome process
    """

    def explore_page(self):
        """python source/main.py chrome --run explore_page
        
        --verify    <VALUE> BOOL | [0] Record not verified      [1] Record Verified
        --fail      <VALUE> BOOL | [0] No loading errors        [1] With loading errors
        --running   <VALUE> BOOL | [0] Record in Execution      [1] Registry not running
        --limit     <VALUE> INT  | [100] Return record quantity
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
        """python source/main.py chrome --run search_duckduckgo_page

        --search    <VALUE> STR  | [Whatever] Word to be searched, ex: 'duckduckgo'.
        --page      <VALUE> INT  | [5] Number of pages to scroll.
        --headless  <VALUE> BOOL | [0] To open browser [1] Background browser.
        """
        chrome_search_duckduckgo_page(
            search=self.search,
            page=self.page,
            headless=bool(self.headless)
        )


    def search_google_page(self):
        """python source/main.py chrome --run search_google_page
        
        --search    <VALUE> STR  | [Whatever] Word to be searched, ex: 'google'.
        --page      <VALUE> INT  | [5] Number of pages to scroll.
        --headless  <VALUE> BOOL | [0] To open browser [1] Background browser.
        """
        chrome_search_google_page(
            search=self.search,
            page=self.page,
            headless=bool(self.headless)
        )
