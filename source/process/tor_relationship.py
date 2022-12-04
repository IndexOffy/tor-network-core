"""
Process Tor
"""

import logging

from base.api import RequestLinks, RequestConnections
from browser.construct import ConstructTorPages


def tor_search_relationship(data: list):
    browser = ConstructTorPages(headless=False)

    request_link = RequestLinks(max_attempt=0)
    request_connection = RequestConnections(max_attempt=0)
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
                big_data = browser.execute_page_link(link=url)
                list_links = big_data.get("list_links")

                for item in list_links:
                    response = request_link.make_get(params=dict(link=item))

                    if response.status_code == 200:
                        data_connection = response.json()[0]

                        request_connection.make_post(
                            payload=dict(
                                id_link=link.get("id"),
                                id_href=data_connection.get("id"),
                                status=True
                            )
                        )
                        logging.info(f" {item}")

            except Exception as error:
                log_error = error.msg if hasattr(error, 'msg') else error
                logging.error(log_error)

            finally:
                request_link.make_put(
                    params=dict(link=url),
                    payload=dict(
                        running=False,
                        login=True
                    )
                )

    finally:
        browser.instance.quit()
