import json
from requests import request, HTTPError


class BaseRequest():
    """Base class request
    """

    def __init__(self, url: str = None) -> None:
        self.url = url
        self.headers = None
        self.setup()

    def setup(self):
        self.load_url()
        self.load_headers()

    def load_headers(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def load_url(self):
        self.url = self.url

    def make_request(self,
            method: str,
            params: dict = dict(),
            payload: dict = dict(),
            headers: dict = None,
            url: str = None,
            attempt: int = 0,
            max_attempt: int = 5) -> request:
        """Make Request
        """
        payload = json.dumps(payload)
        headers = headers or self.headers
        url = url or self.url

        kwargs = {
            'method': method,
            'params': params,
            'data': payload,
            'headers': headers,
            'url': url
        }

        with request(**kwargs) as response:
            http_response = response
            try:
                response.raise_for_status()

            except HTTPError as error:
                print(error)

                if attempt < max_attempt:
                    attempt += 1
                    http_response = self.make_request(
                        method=method,
                        params=params,
                        payload=payload,
                        headers=headers,
                        attempt=attempt
                    )

            return http_response

    def make_get(self,
            params: dict = {},
            url: str = None,
            model_id: str = None) -> request:
        """Make GET
        """
        if not url:
            url = self.url

        if model_id:
            url = "{url}/{model_id}".format(
                url=url,
                model_id=model_id
            )

        return self.make_request(
            method='GET',
            params=params,
            url=url
        )

    def make_post(self,
            payload: dict,
            headers: dict = None,
            url: str = None) -> request:
        """Make POST
        """
        return self.make_request(
            method='POST',
            headers=headers,
            payload=payload,
            url=url,
        )

    def make_put(self,
            payload: dict,
            model_id: int = None,
            params: dict = None,
            headers: dict = None,
            url: str = None) -> request:
        """Make PUT
        """
        if not url:
            url = self.url

        if model_id:
            url = "{url}{model_id}".format(
                url=url,
                model_id=model_id
            )

        return self.make_request(
            method='PUT',
            headers=headers,
            payload=payload,
            params=params,
            url=url,
        )
