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
            header: dict = None,
            url: str = None) -> request:
        """Make Request
        """
        payload = json.dumps(payload)

        kwargs = {
            'method': method,
            'params': params,
            'data': payload,
            'headers': header or self.headers,
            'url': url or self.url
        }

        with request(**kwargs) as response:
            http_response = response
            try:
                response.raise_for_status()

            except HTTPError as error:
                print(error)

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
            header: dict = None,
            url: str = None) -> request:
        """Make POST
        """
        return self.make_request(
            method='POST',
            header=header,
            payload=payload,
            url=url,
        )

    def make_put(self,
            payload: dict,
            model_id: int = None,
            params: dict = None,
            header: dict = None,
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
            header=header,
            payload=payload,
            params=params,
            url=url,
        )
