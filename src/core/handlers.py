from bs4 import BeautifulSoup

from core.spider import Spider
from settings import URL_API
from core.request import BaseRequest
from core.browser import get_chrome_browser, get_tor_browser
from core.log import logging


class Handler(object):

    def __init__(self, headless=True) -> None:
        self.request = BaseRequest(url=URL_API)
        self.headless = headless
        self.instance = None
        self.domain = None
        self.ssl = None

    def execute(self, link: str):
        self.instance.get(link)

        page_source = BeautifulSoup(self.instance.page_source, "html.parser")
        worker = Spider(url=link,page_source=page_source)

        list_pages = worker.set_page_links(domain=self.domain, ssl=self.ssl)

        for item in list_pages:
            data = dict(link=item)

            response = self.request.make_get(params=data)
            if response.status_code == 204:
                logging.info(item)
                self.request.make_post(payload=data)


class HandlerChromePages(Handler):
    
    def __init__(self, headless=True) -> None:
        super().__init__(headless)
        self.instance = get_chrome_browser(headless=self.headless)
        self.domain = ".com"
        self.ssl = True


class HandlerTorPages(Handler):
    
    def __init__(self, headless=False) -> None:
        super().__init__(headless)
        self.instance = get_tor_browser(headless=self.headless)
        self.domain = ".onion"
        self.ssl = False
