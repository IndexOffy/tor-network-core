import logging

from base.api import RequestLinks, RequestSubpages
from browser.construct import ConstructTorPages


def process_subpage_tor(request_page, request_subpage, data: list):
    browser = ConstructTorPages()
    list_links = list()

    try:
        for link in data:
            request_subpage.make_put(
                payload=dict(running=True),
                model_id=link.get("id")
            )

        for link in data:
            log_error = None
            page_link = link.get("link")

            try:
                big_data = browser.execute_page(link=page_link)
                list_links = big_data.get("list_links")

                for item in list_links:
                    print(item)

                    params = dict(link=item)
                    response = request_page.make_get(params=params)

                    if response.status_code == 204:
                        request_page.make_post(payload=params)

            except Exception as error:
                log_error = error.msg if hasattr(error, 'msg') else error
                logging.error(log_error)

                request_subpage.make_put(
                    params=dict(link=page_link),
                    payload=dict(
                        fail=True
                    )
                )

            finally:
                request_subpage.make_put(
                    params=dict(link=page_link),
                    payload=dict(
                        running=False,
                        verify=True
                    )
                )

    finally:
        browser.instance.quit()


if __name__ == "__main__":
    request_page = RequestLinks()
    request_subpage = RequestSubpages()

    response = request_subpage.make_get(
        params=dict(
            verify=0,
            fail=0,
            running=0,
            limit=50,
            order_by='asc'
        )
    )

    if response.status_code == 200:
        process_subpage_tor(
            request_page=request_page,
            request_subpage=request_subpage,
            data=response.json()
        )
