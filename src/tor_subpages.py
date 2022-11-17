from settings import URL_API
from helpers.log import logging
from core.handlers import HandlerTorPages
from helpers.request import BaseRequest


def process_subpage_tor(request, data: list):
    browser = HandlerTorPages()
    list_links = list()

    try:
        for link in data:
            model_id = link.get("id")
            request.make_put(
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
                    print(item)

            except Exception as error:
                log_error = error.msg if hasattr(error, 'msg') else error
                logging.error(log_error)

    finally:
        browser.instance.quit()


if __name__ == "__main__":
    request = BaseRequest(url=URL_API)
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
        process_subpage_tor(request=request, data=response.json())
