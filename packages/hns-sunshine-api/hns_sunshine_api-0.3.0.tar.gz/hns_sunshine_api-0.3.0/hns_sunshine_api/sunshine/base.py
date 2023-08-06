import requests


class SunshineBase:
    _OBJECTS_ROOT = 'api/sunshine/objects'

    _RELATIONSHIPS_ROOT = 'api/sunshine/relationships'

    _HEADERS = {
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
        self._objects_base_url = f'https://{self.subdomain}.zendesk.com/{self._OBJECTS_ROOT}'
        self._relationships_base_url = f'https://{self.subdomain}.zendesk.com/{self._RELATIONSHIPS_ROOT}'

        self._session = requests.Session()
        self._session.headers.update(self._HEADERS)
        self._session.auth = (f'{email}/token', f'{key}')

    def __repr__(self):
        return f'SunshineBase(subdomain="{self.subdomain}")'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def close_session(self):
        """ Closes requests session """

        self._session.close()
