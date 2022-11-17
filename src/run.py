from src.settings import URL_API
from src.core.log import logging
from src.core.handlers import HandlerTorPages
from src.core.request import BaseRequest


def process_tor(request, data: list):
    browser = HandlerTorPages()

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
                browser.execute(link=url)
            except Exception as error:
                log_error = error.msg
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
            limit=50
        )
    )

    if response.status_code == 200:
        process_tor(request=request, data=response.json())
