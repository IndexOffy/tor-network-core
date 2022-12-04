from base.api import RequestLinks, RequestSubpages
from base.command import BaseCommand
from process import (
    tor_search_page,
    tor_search_relationship,
    tor_search_subpage
)


class CommandTor(BaseCommand):
    """Command Tor process
    """

    def search_page(self):
        """python source/main.py tor --run search_page

        --verify 0
        --fail 0
        --running 0
        --limit 100
        """
        response = RequestLinks().make_get(
            params=dict(
                verify=self.verify,
                fail=self.fail,
                running=self.running,
                limit=self.limit,
                order_by='asc',
                title='null'
            )
        )
        if response.status_code == 200:
            tor_search_page(data=response.json())

    def search_relationship(self):
        """python source/main.py tor --run search_relationship

        --verify 0
        --fail 0
        --running 0
        --limit 100
        """
        response = RequestLinks().make_get(
            params=dict(
                verify=self.verify,
                running=self.running,
                limit=self.limit,
                order_by='asc',
                login=0
            )
        )
        if response.status_code == 200:
            tor_search_relationship(data=response.json())

    def search_subpage(self):
        """python source/main.py tor --run search_subpage

        --verify 0
        --fail 0
        --running 0
        --limit 100
        """
        response = RequestSubpages().make_get(
            params=dict(
                verify=self.verify,
                fail=self.fail,
                running=self.running,
                limit=self.limit,
                order_by='asc',
                explored=0
            )
        )
        if response.status_code == 200:
            tor_search_subpage(data=response.json())
