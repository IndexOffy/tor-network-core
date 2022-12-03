from base.api import RequestLinks, RequestConnections
from base.process import BaseProcess
from base.handlers import BaseHandler
from browser.construct import ConstructTorPages


class HandlerTorRelationship(BaseHandler):

    def run(self):
        big_data = self.browser.execute_page_link(link=self.link.get("link"))
        list_links = big_data.get("list_links")

        for item in list_links:
            response = request.make_get(params=dict(link=item))

            if response.status_code == 200:
                data_connection = response.json()

                RequestConnections().make_post(
                    payload=dict(
                        id_link=self.link.get("id"),
                        id_href=data_connection.get("id"),
                        status=True
                    )
                )

if __name__ == "__main__":
    request = RequestLinks()
    response = request.make_get(
        params=dict(
            verify=0,
            fail=0,
            running=0,
            title='null',
            limit=5
        )
    )
    process = BaseProcess(browser=ConstructTorPages)
    if response.status_code == 200:
        process.run(handler=HandlerTorRelationship, request=request, data=response.json())
