"""
Zendesk sunshine API
API guide: https://developer.zendesk.com/rest_api/docs/sunshine/introduction
"""
from hns_sunshine_api.sunshine.objects import SunshineObjects
from hns_sunshine_api.sunshine.relationships import SunshineRelationships


class Sunshine(SunshineObjects, SunshineRelationships):

    def __init__(self, subdomain: str, email: str, key: str):
        """
        Creates and manages objects on zendesk sunshine

        Instantiating creates a requests session. You can call `close` at the end.

        Usage:

        Simple use:

            sunshine = Sunshine(subdomain='mydomain')
            resp1 = sunshine.get('http://myapi.com/get1)
            resp2 = sunshine.get('http://myapi.com/get2)
            sunshine.close_session()

        Using context manager:

            with Sunshine(subdomain='mydomain') as sunshine:
                resp1 = sunshine.get('http://myapi.com/get1)
                resp2 = sunshine.get('http://myapi.com/get2)

        Zendesk API docs: https://developer.zendesk.com/rest_api/docs/sunshine/introduction
        :param subdomain: Your zendesk subdomain
        :param email: Sunshine user email ID. Used for token based authentication
        :param key: Sunshine token.
        """

        super().__init__(subdomain, email, key)

    def __repr__(self):
        return f'Sunshine(subdomain="{self.subdomain}")'
