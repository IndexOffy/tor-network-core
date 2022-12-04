"""
Process Tor
"""


import logging

from base.api import RequestLinks, RequestSubpages
from browser.construct import ConstructTorPages


def tor_search_subpage(data: list):
    browser = ConstructTorPages(headless=False)

    request_link = RequestLinks(max_attempt=0)
    request_subpage = RequestSubpages(max_attempt=0)
    list_links = list()

    try:
        for link in data:
            request_link.make_put(
                params=dict(id=link.get("id")),
                payload=dict(running=True)
            )

        for link in data:
            log_error = None
            url = link.get("link")
            try:
                big_data = browser.execute_subpage_link(link=url)
                list_links = big_data.get("list_links")

                for item in list_links:
                    data = dict(link=item)
                    print(item)

                    response = request_subpage.make_get(params=data)
                    if response.status_code == 204:
                        logging.info(f" {item}")
                        request_subpage.make_post(payload=data)

            except Exception as error:
                log_error = error.msg if hasattr(error, 'msg') else error
                logging.error(log_error)

            finally:
                explored = True
                if log_error:
                    error_lit = [
                        'Browsing context has been discarded',
                        'Failed to decode response from marionette',
                        'Tried to run command without establishing a connection'
                    ]
                    if log_error in error_lit:
                        explored = False

                request_link.make_put(
                    params=dict(link=url),
                    payload=dict(
                        explored=explored,
                        running=False
                    )
                )

    finally:
        browser.instance.quit()
