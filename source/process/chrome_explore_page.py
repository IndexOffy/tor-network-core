"""
Process Chrome
"""


import logging

from base.api import RequestLinks, RequestUrls
from browser.construct import ConstructChromePages


def chrome_explore_page(data: list, headless: bool = True):
    browser = ConstructChromePages(headless=headless)
    browser.domain = ".onion"
    browser.ssl = False

    request_url = RequestUrls(max_attempt=0)
    request_link = RequestLinks(max_attempt=0)
    list_links = list()

    try:
        for link in data:
            request_url.make_put(
                params=dict(id=link.get("id")),
                payload=dict(running=True)
            )

        for link in data:
            log_error = None
            url = link.get("link")
            try:
                big_data = browser.execute_page_link(link=url)
                list_links = big_data.get("list_links")

                for item in list_links:
                    request_link.make_post(payload=dict(link=item))
                    print(item)

            except Exception as error:
                log_error = error.msg if hasattr(error, 'msg') else error
                logging.error(log_error)

                request_url.make_put(
                    params=dict(link=url),
                    payload=dict(
                        fail=True
                    )
                )

            finally:
                verify = True
                if log_error:
                    error_lit = [
                        'Browsing context has been discarded',
                        'Failed to decode response from marionette',
                        'Tried to run command without establishing a connection'
                    ]
                    if log_error in error_lit:
                        verify = False

                request_url.make_put(
                    params=dict(link=url),
                    payload=dict(
                        verify=verify,
                        running=False
                    )
                )

    finally:
        browser.instance.quit()
