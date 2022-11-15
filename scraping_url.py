from bs4 import BeautifulSoup

from src.browser import Browser

link = 'https://thehiddenwiki.org/'
instance = Browser(driver='tor')
instance.driver.get(link)

full_html = instance.driver.page_source
resp = BeautifulSoup(full_html, "html.parser")

links = resp.find_all('a')
list_links = list()

print(instance.driver.title)

keywords = resp.find("meta", {"name":"keywords"})
author = resp.find("meta", {"name":"author"})

keywords = keywords.get("content") if keywords else None
keywords = author.get("content") if author else None

for link in links:
    full_link = link.get("href")
    try:
        len_string = full_link.find(".onion")

        if len_string > 0:
            full_link = full_link[0:len_string + 6]
            list_links.append(full_link)

    except Exception as error:
        pass

list_links = set(list_links)

for item in list_links:
    print(item)

instance.driver.quit()