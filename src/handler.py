from bs4 import BeautifulSoup
from src.settings import URL_API
from src.request import BaseRequest
from src.browser import get_chrome_browser, get_tor_browser


class Handler():

    def __init__(self, driver: str = 'tor', headless=False) -> None:
        self.request = BaseRequest(url=URL_API)

        if driver == 'tor':
            self.instance = get_tor_browser(headless=headless)
        else:
            self.instance = get_chrome_browser(headless=headless)

    def execute(self, link: str, timeout: int = 15):
        self.instance.implicitly_wait(time_to_wait=timeout)
        self.instance.get(link)

        full_html =  self.instance.page_source
        resp = BeautifulSoup(full_html, "html.parser")

        keywords = resp.find("meta", {"name":"keywords"})
        author = resp.find("meta", {"name":"author"})

        data_title = self.instance.title
        data_author = author.get("content") if author else None
        data_keywords = keywords.get("content") if keywords else None

        self.request.make_put(
            params=dict(link=link),
            payload=dict(
                title=data_title,
                author=data_author,
                keywords=data_keywords,
                verify=1
            )
        )

        links = resp.find_all('a')
        list_links = self.get_links(links=links)
        self.update_links(list_links=list_links)

    def get_links(self, links: list):
        list_links = list()

        for link in links:
            full_link = link.get("href")
            print(full_link)

            try:
                len_string = full_link.find(".onion")

                if len_string > 0:
                    full_link = full_link[0:len_string + 6]
                    list_links.append(full_link)

            except Exception as error:
                print(error)

        return set(list_links)

    def update_links(self, list_links: list):

        for item in list_links:
            response = self.request.make_get(params=dict(link=item))

            if response.status_code == 204:
                payload = {"link": item}
                self.request.make_post(payload=payload)
