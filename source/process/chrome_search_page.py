"""
Process Chrome
"""


import logging
from time import sleep

from selenium.webdriver.common.by import By
from browser.construct import ConstructChromePages


def chrome_search_page():
    link = 'https://duckduckgo.com/'
    browser = ConstructChromePages(headless=True, link=link)

    try:
        search = browser.instance.find_element("name", "q")
        search.send_keys("links deep web")
        search.submit()

        for index, page in enumerate(range(5), 1):
            browser.instance.find_element("id", f"rld-{index}").click()
            browser.instance.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(1)

        articles = browser.instance.find_elements(By.TAG_NAME, "article")

        for article in articles:
            article_title = article.find_element(By.TAG_NAME, "h2")
            link = article_title.find_element(By.TAG_NAME, "a")

            print(link.get_attribute("href"))

    except Exception as error:
        log_error = error.msg if hasattr(error, 'msg') else error
        logging.error(log_error)

    finally:
        browser.instance.quit()
