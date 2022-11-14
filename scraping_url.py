from spider import BaseSource
from bs4 import BeautifulSoup

link = 'https://github.com/IndexOffy'
instance = BaseSource()
instance.driver.get(link)

full_html = instance.driver.page_source
resp = BeautifulSoup(full_html, "html.parser")

links = resp.find_all('a')

for link in links:
    print(link.get("href"))
