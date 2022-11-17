from settings import URL_API
from src.settings.log import logging
from core.handlers import HandlerTorPages
from src.helpers.request import BaseRequest


def process_page_tor(request, data: list):
    browser = HandlerTorPages()
    content = dict()
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
                big_data = browser.execute_page(link=url)
                content = big_data.get("content")
                list_links = big_data.get("list_links")

                for item in list_links:
                    data = dict(link=item)
                    print(item)

                    response = request.make_get(params=data)
                    if response.status_code == 204:
                        logging.info(item)
                        request.make_post(payload=data)

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
                    params=dict(link=url),
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
        process_page_tor(request=request, data=response.json())
