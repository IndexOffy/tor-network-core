import logging


class BaseProcess():

    def __init__(self, browser) -> None:
        self.browser = browser

    def run(self, handler, request, data: list):
        browser = self.browser(headless=False)
        try:
            for link in data:
                request.make_put(
                    params=dict(id=link.get("id")),
                    payload=dict(running=True)
                )

            for link in data:
                log_error = None
                try:
                    handler(browser=browser, link=link)
                except Exception as error:
                    log_error = error.msg if hasattr(error, 'msg') else error
                    logging.error(log_error)

                finally:
                    verify = False
                    if log_error:
                        error_lit = [
                            'Browsing context has been discarded',
                            'Failed to decode response from marionette',
                            'Tried to run command without establishing a connection'
                        ]
                        if log_error in error_lit:
                            verify = False

                    request.make_put(
                        params=dict(link=link.get("link")),
                        payload=dict(
                            verify=verify,
                            running=False
                        )
                    )

        finally:
            browser.instance.quit()
