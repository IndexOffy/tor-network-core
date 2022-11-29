import logging

from base.api import RequestLinks, RequestConnections
from browser.construct import ConstructTorPages


def process_relationship_tor(request, data: list):
    browser = ConstructTorPages()
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
                list_links = big_data.get("list_links")

                for item in list_links:
                    response = request.make_get(params=dict(link=item))

                    if response.status_code == 200:
                        data_connection = response.json()

                        RequestConnections().make_post(
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
                request.make_put(
                    params=dict(link=url),
                    payload=dict(
                        running=False
                    )
                )

    finally:
        browser.instance.quit()


if __name__ == "__main__":
    request = RequestLinks()
    response = request.make_get(
        params=dict(
            verify=1,
            running=0,
            limit=5
        )
    )

    if response.status_code == 200:
        process_relationship_tor(
            request=request,
            data=response.json()
        )
