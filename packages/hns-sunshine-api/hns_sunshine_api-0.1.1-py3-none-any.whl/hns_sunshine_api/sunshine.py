"""
Zendesk sunshine API
API guide: https://developer.zendesk.com/rest_api/docs/sunshine/introduction
"""
import requests


class Sunshine:

    OBJECTS_ROOT = 'api/sunshine/objects'

    RELATIONSHIPS_ROOT = 'api/sunshine/relationships'

    HEADERS = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

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

        self.subdomain = subdomain
        self.objects_base_url = f'https://{self.subdomain}.zendesk.com/{self.OBJECTS_ROOT}'
        self.relationships_base_url = f'https://{self.subdomain}.zendesk.com/{self.RELATIONSHIPS_ROOT}'

        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        self.session.auth = (f'{email}/token', f'{key}')

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def __repr__(self):
        return f'Sunshine(subdomain="{self.subdomain}")'

    def close_session(self):
        """ Closes requests session """

        self.session.close()

    def list_object_records(self, object_type: str, external_id: str = None) -> dict:
        """
        Gets object records from sunshine
        :param object_type: Type of object record
        :param external_id: external ID for the object record
        :return: Object record
        """

        if external_id:
            params = {
                'type': object_type,
                'external_id': external_id
            }
        else:
            params = {
                'type': object_type
            }
        resp = self.session.get(f'{self.objects_base_url}/records', params=params)
        return resp.json()

    def list_related_objects_records(self, object_id: str, relationship_key: str) -> dict:
        """
        Returns all the object records that the specified object record has relationship records with for the
        specified relationship type
        :param object_id: Object record ID
        :param relationship_key: Relationship type key
        :return: All the object records related to the relationship key
        """

        resp = self.session.get(f'{self.objects_base_url}/records/{object_id}/related/{relationship_key}')
        return resp.json()

    def show_object_record(self, object_id: str) -> dict:
        """
        Returns the specified object record
        :param object_id: Object record ID
        :return: Object record
        """

        resp = self.session.get(f'{self.objects_base_url}/records/{object_id}')
        return resp.json()

    def create_object_record(self, record_data: dict) -> dict:
        """
        Creates an object record.
        :param record_data: Object record data.
        Check https://developer.zendesk.com/rest_api/docs/sunshine/resources#json-format for details
        :return: Object record
        """

        resp = self.session.post(f'{self.objects_base_url}/records', json=record_data)
        return resp.json()

    def update_object_record(self, object_id: str, data: dict) -> dict:
        """
        Updates the attributes object of the specified object record. It does not update any other record properties.

        The attributes object patches the previously stored object. Therefore, the request should only contain the
        properties of the attributes object that need to be updated.

        The request must include an "application/merge-patch+json" content-type header.

        :param object_id: Object record ID
        :param data: Object record
        :return: Updated object record
        """

        self.session.headers['Content-type'] = 'application/merge-patch+json'
        resp = self.session.patch(f'{self.objects_base_url}/records/{object_id}', json=data)
        return resp.json()

    def update_object_record_by_external_id(self, data: dict) -> dict:
        """
        Creates a new object if an object with given external id does not exist and updates the attributes object of
        the specified object record if an object with the given external id does exist.
        This endpoint does not update any other record properties.

        The request data should contain:
            - Object type
            - External id
            - attributes of the object that needs to be updated
        The request must include an "application/merge-patch+json" content-type header.

        :param data: Object record
        :return: Updated object record
        """

        self.session.headers['Content-type'] = 'application/merge-patch+json'
        resp = self.session.patch(f'{self.objects_base_url}/records', json=data)
        return resp.json()

    def delete_object_record(self, object_id: str) -> dict:
        """
        Deletes the specified object record.

        Before deleting an object record, you must delete any relationship record that specifies the object record

        :param object_id: Object record ID
        :return: Nothing
        """

        resp = self.session.delete(f'{self.objects_base_url}/records/{object_id}')
        return resp.json()

    def list_relationship_records_by_object_record(self, object_id: str, relationship_type: str) -> dict:
        """
        Returns the relationship records of a specified relationship type for a specified object record.
        For the type, specify a relationship type key. For the object record id, specify a custom object
        record id or a Zendesk object record id.
        The record id must be the relationship record's source record id, not its target record id.

        :param object_id: Object record ID
        :param relationship_type: Relationship type key
        :return: Relationship record
        """

        resp = self.session.get(f'{self.objects_base_url}/records/{object_id}/relationships/{relationship_type}')
        return resp.json()

    def list_relationship_records_by_type(self, relationship_type: str) -> dict:
        """
        Returns all the relationship records of the specified relationship type.
        For the type, specify a relationship type key.
        :param relationship_type: Relationship type key
        :return: Relationship records
        """

        resp = self.session.get(f'{self.relationships_base_url}/records', params={'type': relationship_type})
        return resp.json()

    def show_relationship_record_by_id(self, relationship_id: str) -> dict:
        """
        Returns a relationship record specified by id
        :param relationship_id: Relationship type key
        :return: Relationship record
        """

        resp = self.session.get(f'{self.relationships_base_url}/records/{relationship_id}')
        return resp.json()

    def create_relationship_record(self, record_data: dict) -> dict:
        """
        Creates a relationship record between two object records based on a relationship type.
        The relationship type defines the object types of the two object records.
        :param record_data: Relationship record data.
        Check https://developer.zendesk.com/rest_api/docs/sunshine/relationships#json-format for details
        :return: Relationship record
        """

        resp = self.session.post(f'{self.relationships_base_url}/records', json=record_data)
        return resp.json()

    def delete_relationship_record(self, relationship_id: str) -> dict:
        """
        Deletes a specified relationship record
        :param relationship_id: Relationship object ID
        :return: Nothing
        """

        resp = self.session.delete(f'{self.relationships_base_url}/records/{relationship_id}')
        return resp.json()

