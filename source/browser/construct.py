from bs4 import BeautifulSoup

from browser.spider import BaseSpider
from browser.base import get_chrome_browser, get_tor_browser


class BrowserConstruct(object):

    def __init__(self, headless: bool = True, link: str = None) -> None:
        self.headless = headless
        self.link = link
        self.instance = None
        self.domain = None
        self.ssl = None

    def execute_page_link(self, link: str):
        self.instance.get(link)

        page_source = BeautifulSoup(self.instance.page_source, "html.parser")
        worker = BaseSpider(url=link, page_source=page_source)

        content = worker.get_content()
        list_links = worker.set_page_links(domain=self.domain, ssl=self.ssl)

        return dict(
            content=content,
            list_links=list_links,
            page_source=page_source
        )

    def execute_subpage_link(self, link: str) -> dict:
        self.instance.get(link)

        page_source = BeautifulSoup(self.instance.page_source, "html.parser")
        worker = BaseSpider(url=link, page_source=page_source)

        content = worker.get_content()
        list_links = worker.set_subpage_links()

        return dict(
            content=content,
            list_links=list_links,
            page_source=page_source
        )


class ConstructChromePages(BrowserConstruct):
    
    def __init__(self, headless: bool = True, link: str = None) -> None:
        super().__init__(headless, link)
        self.instance = get_chrome_browser(headless=self.headless)
        self.domain = ".com"
        self.ssl = True

        if link:
            self.instance.get(link)


class ConstructTorPages(BrowserConstruct):
    
    def __init__(self, headless: bool = True, link: str = None) -> None:
        super().__init__(headless, link)
        self.instance = get_tor_browser(headless=self.headless)
        self.domain = ".onion"
        self.ssl = False

        if link:
            self.instance.get(link)
