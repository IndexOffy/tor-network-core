import logging

from base.api import RequestLinks, RequestConnections
from browser.construct import ConstructTorPages


def process_page_tor(request, data: list):
    browser = ConstructTorPages(headless=False)
    content = dict()
    list_links = list()

    try:
        for link in data:
            request.make_put(
                params=dict(id=link.get("id")),
                payload=dict(running=True)
            )

        for link in data:
            log_error = None
            page_id = link.get("id")
            page_link = link.get("link")

            try:
                big_data = browser.execute_page(link=page_link)
                content = big_data.get("content")
                list_links = big_data.get("list_links")

                for item in list_links:
                    params = dict(link=item)
                    response = request.make_get(params=params)
                    logging.info(f" {item}")

                    id_href = None

                    if response.status_code == 204:
                        data_link = request.make_post(payload=params)
                        link = data_link.get("id")

                    if response.status_code == 200:
                        if len(response.json()) == 1:
                            id_href = response.json()[0].get("id")

                    if id_href and page_id != id_href:
                        print(f"{page_id} - {id_href}")
                        RequestConnections().make_post(
                            payload=dict(
                                id_link=page_id,
                                id_href=id_href,
                                status=True
                            )
                        )

            except Exception as error:
                log_error = error.msg if hasattr(error, 'msg') else error
                logging.error(log_error)

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

                request.make_put(
                    params=dict(link=page_link),
                    payload=dict(
                        title=content.get("title"),
                        keywords=content.get("keywords"),
                        author=content.get("author"),
                        verify=verify,
                        running=False
                    )
                )

    finally:
        browser.instance.quit()


if __name__ == "__main__":
    request = RequestLinks()
    response = request.make_get(
        params=dict(
            verify=0,
            fail=0,
            running=0,
            title='null',
            limit=5
        )
    )

    if response.status_code == 200:
        process_page_tor(request=request, data=response.json())
