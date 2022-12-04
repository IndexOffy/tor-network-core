"""
Process Chrome
"""


import logging
from time import sleep

from selenium.webdriver.common.by import By

from base.api import RequestUrls
from browser.construct import ConstructChromePages


def chrome_search_duckduckgo_page(search: str, page: int):
    domain = 'https://duckduckgo.com/'
    browser = ConstructChromePages(headless=True, link=domain)

    try:
        input_search = browser.instance.find_element("name", "q")
        input_search.send_keys(search)
        input_search.submit()

        for index, page in enumerate(range(page), 1):
            browser.instance.find_element("id", f"rld-{index}").click()
            browser.instance.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(1)

        articles = browser.instance.find_elements(By.TAG_NAME, "article")

        for article in articles:
            article_title = article.find_element(By.TAG_NAME, "h2")
            link = article_title.find_element(By.TAG_NAME, "a")

            url = link.get_attribute("href")
            RequestUrls().make_post(payload=dict(link=url))
            print(url)

    except Exception as error:
        log_error = error.msg if hasattr(error, 'msg') else error
        logging.error(log_error)

    finally:
        browser.instance.quit()


def chrome_search_google_page(search: str, page: int):
    domain = 'https://google.com/'
    browser = ConstructChromePages(headless=True, link=domain)

    try:
        input_search = browser.instance.find_element("name", "q")
        input_search.send_keys(search)
        input_search.submit()

        articles = browser.instance.find_elements(By.CLASS_NAME, "g")
        for article in articles:
            link = article.find_element(By.TAG_NAME, "a")

            url = link.get_attribute("href")
            RequestUrls().make_post(payload=dict(link=url))
            print(url)

    except Exception as error:
        log_error = error.msg if hasattr(error, 'msg') else error
        logging.error(log_error)

    finally:
        browser.instance.quit()
