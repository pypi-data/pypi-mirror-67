import requests


class SunshineBase:
    OBJECTS_ROOT = 'api/sunshine/objects'

    RELATIONSHIPS_ROOT = 'api/sunshine/relationships'

    HEADERS = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    def __init__(self, subdomain: str, email: str, key: str):
        """
        Creates and manages objects on zendesk sunshine

        :param subdomain: Your zendesk subdomain
        :param email: Sunshine user email ID. Used for token based authentication
        :param key: Sunshine token.
        """

        self.subdomain = subdomain
        self.objects_base_url = f'https://{self.subdomain}.zendesk.com/{self.OBJECTS_ROOT}'
        self.relationships_base_url = f'https://{self.subdomain}.zendesk.com/{self.RELATIONSHIPS_ROOT}'

        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        self.session.auth = (f'{email}/token', f'{key}')

    def __repr__(self):
        return f'SunshineBase(subdomain="{self.subdomain}")'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def close_session(self):
        """ Closes requests session """

        self.session.close()
