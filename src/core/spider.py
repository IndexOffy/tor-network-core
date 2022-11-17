from bs4 import BeautifulSoup
from helpers.log import logging


class Spider(object):

    def __init__(self, url: str, page_source: BeautifulSoup) -> None:
        self.url = url
        self.page_source = page_source

    @staticmethod
    def search_links(page_source: BeautifulSoup) -> list:
        list_links = list()
        links = page_source.find_all('a')

        for link in links:
            full_link = link.get("href")

            if full_link:
                list_links.append(full_link)

        return list_links

    @staticmethod
    def check_page_link(url: str, domain: str, ssl: bool = True) -> str:
        ssl = "https://" if ssl == True else "http://"
        try:
            len_start_string = url.find(ssl)
            len_end_string = url.find(domain)

            if len_end_string > 0:
                url = url[0:len_end_string + len(domain)]

                if len_start_string == 0:
                    return url

        except Exception as error:
            logging.error(error.msg)

    @staticmethod
    def check_subpage_link(url: str, page: str) -> str:
        if page[-1:] == "/":
            page = page[0:len(page)-1]

        for check in ["/", "#"]:
            if url[0:1] == check:
                response = f"{page}{url}"
                if url[0:4] != "http":
                    return response

        for check in [".php", ".html"]:
            if url[-len(check):len(url)] == check:
                response = f"{page}/{url.replace('./','')}"
                if url[0:4] != "http":
                    return response

    def get_content(self) -> dict:
        keywords = self.page_source.find("meta", {"name":"keywords"})
        author = self.page_source.find("meta", {"name":"author"})

        data_title = self.page_source.title.text

        data_author = author.get("content") if author else None
        data_keywords = keywords.get("content") if keywords else None

        return dict(
            title=data_title,
            keywords=data_author,
            author=data_keywords
        )

    def set_page_links(self, domain: str, ssl: bool) -> set:
        list_links = list()

        list_pages = self.search_links(page_source=self.page_source)

        for item in list_pages:
            link = self.check_page_link(url=item, domain=domain, ssl=ssl)
            if link:
                list_links.append(link)

        return set(list_links)

    def set_subpage_links(self) -> set:
        list_links = list()

        list_subpages = self.search_links(page_source=self.page_source)

        for item in list_subpages:
            link = self.check_subpage_link(url=item, page=self.url)
            if link:
                list_links.append(link)

        return set(list_links)
