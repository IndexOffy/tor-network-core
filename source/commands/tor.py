"""
Tor Commands Module
"""


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

        --verify    <VALUE> BOOL | [0] Record not verified      [1] Record Verified
        --fail      <VALUE> BOOL | [0] No loading errors        [1] With loading errors
        --running   <VALUE> BOOL | [0] Record in Execution      [1] Registry not running
        --limit     <VALUE> INT  | [100] Return record quantity
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

        --verify    <VALUE> BOOL | [0] Record not verified      [1] Record Verified
        --fail      <VALUE> BOOL | [0] No loading errors        [1] With loading errors
        --running   <VALUE> BOOL | [0] Record in Execution      [1] Registry not running
        --limit     <VALUE> INT  | [100] Return record quantity
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

        --verify    <VALUE> BOOL | [0] Record not verified      [1] Record Verified
        --fail      <VALUE> BOOL | [0] No loading errors        [1] With loading errors
        --running   <VALUE> BOOL | [0] Record in Execution      [1] Registry not running
        --limit     <VALUE> INT  | [100] Return record quantity
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
