from bs4 import BeautifulSoup

from core.spider import Spider
from core.browser import get_chrome_browser, get_tor_browser


class Handler(object):

    def __init__(self, headless=True) -> None:
        self.headless = headless
        self.instance = None
        self.domain = None
        self.ssl = None

    def execute_page(self, link: str):
        self.instance.get(link)

        page_source = BeautifulSoup(self.instance.page_source, "html.parser")
        worker = Spider(url=link, page_source=page_source)

        content = worker.get_content()
        list_links = worker.set_page_links(domain=self.domain, ssl=self.ssl)

        return dict(
            content=content,
            list_links=list_links
        )

    def execute_subpage(self, link: str) -> dict:
        self.instance.get(link)

        page_source = BeautifulSoup(self.instance.page_source, "html.parser")
        worker = Spider(url=link, page_source=page_source)

        content = worker.get_content()
        list_links = worker.set_subpage_links()

        return dict(
            content=content,
            list_links=list_links
        )


class HandlerChromePages(Handler):
    
    def __init__(self, headless=True) -> None:
        super().__init__(headless)
        self.instance = get_chrome_browser(headless=self.headless)
        self.domain = ".com"
        self.ssl = True


class HandlerTorPages(Handler):
    
    def __init__(self, headless=True) -> None:
        super().__init__(headless)
        self.instance = get_tor_browser(headless=self.headless)
        self.domain = ".onion"
        self.ssl = False
