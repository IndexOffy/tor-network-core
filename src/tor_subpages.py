from settings import URL_API_PAGE, URL_API_SUBPAGE
from helpers.log import logging
from core.handlers import HandlerTorPages
from helpers.request import BaseRequest


def process_subpage_tor(request_page, request_subpage, data: list):
    browser = HandlerTorPages()
    list_links = list()

    try:
        for link in data:
            model_id = link.get("id")
            request_page.make_put(
                params=dict(id=model_id),
                payload=dict(running=True)
            )

        for link in data:
            log_error = None
            url = link.get("link")
            try:
                big_data = browser.execute_subpage(link=url)
                list_links = big_data.get("list_links")

                for item in list_links:
                    data = dict(link=item)

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

                request_page.make_put(
                    params=dict(link=url),
                    payload=dict(
                        explored=explored,
                        running=False
                    )
                )

    finally:
        browser.instance.quit()


if __name__ == "__main__":
    request_page = BaseRequest(url=URL_API_PAGE)
    request_subpage = BaseRequest(url=URL_API_SUBPAGE)

    response = request_page.make_get(
        params=dict(
            verify=1,
            fail=0,
            running=0,
            explored=0,
            limit=10
        )
    )

    if response.status_code == 200:
        process_subpage_tor(
            request_page=request_page,
            request_subpage=request_subpage,
            data=response.json()
        )