from src.handler import Handler
from src.request import BaseRequest
from src.settings import URL_API


def process_tor():
    instance = Handler()
    request = BaseRequest(url=URL_API)

    response = request.make_get(
        params=dict(
            verify=False,
            fail=False,
            running=False,
            limit=10
        )
    )

    def load(url):
        try:
            instance.execute(link=url)
        except Exception as error:
            print(error)

            error_lit = [
                'Browsing context has been discarded',
                'Failed to decode response from marionette'
            ]

            try:
                link = request.make_get(params=dict(link=url))
                attempts = int(link.json()[0].get("attempts")) + 1

                if not error.msg in error_lit:
                    if link.status_code == 200:
                        request.make_put(
                            params=dict(link=url),
                            payload=dict(
                                verify=True,
                                fail=True,
                                attempts=attempts
                            )
                        )

            except Exception as error:
                print(error)

        finally:
            request.make_put(
                params=dict(link=url),
                payload=dict(
                    running=False
                )
            )

    if response.status_code == 200:
        data = response.json()

        for link in data:
            model_id = link.get("id")
            request.make_put(
                params=dict(id=model_id),
                payload=dict(running=True)
            )

        for link in data:
            load(link.get("link"))

    instance.instance.quit()


if __name__ == "__main__":
    process_tor()
