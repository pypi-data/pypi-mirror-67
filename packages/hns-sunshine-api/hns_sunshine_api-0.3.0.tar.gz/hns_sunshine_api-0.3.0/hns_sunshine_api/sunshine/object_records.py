from hns_sunshine_api.sunshine.base import SunshineBase
from requests import Response


class SunshineObjectRecords(SunshineBase):
    """ Sunshine Objects class """

    def __init__(self, subdomain: str, email: str, key: str):
        super().__init__(subdomain, email, key)

    def __repr__(self):
        return f'SunshineObjectRecords(subdomain="{self.subdomain}")'

    def list(self, object_type: str, external_id: str = None) -> Response:
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
        return self._session.get(f'{self._objects_base_url}/records', params=params)

    def list_related(self, object_id: str, relationship_key: str) -> Response:
        """
        Returns all the object records that the specified object record has relationship records with for the
        specified relationship type
        :param object_id: Object record ID
        :param relationship_key: Relationship type key
        :return: All the object records related to the relationship key
        """

        resp = self._session.get(f'{self._objects_base_url}/records/{object_id}/related/{relationship_key}')
        return resp.json()

    def show(self, object_id: str) -> Response:
        """
        Returns the specified object record
        :param object_id: Object record ID
        :return: Object record
        """

        return self._session.get(f'{self._objects_base_url}/records/{object_id}')

    def create(self, record_data: dict) -> Response:
        """
        Creates an object record.
        :param record_data: Object record data.
        Check https://developer.zendesk.com/rest_api/docs/sunshine/resources#json-format for details
        :return: Object record
        """

        return self._session.post(f'{self._objects_base_url}/records', json=record_data)

    def update(self, object_id: str, data: dict) -> Response:
        """
        Updates the attributes object of the specified object record. It does not update any other record properties.

        The attributes object patches the previously stored object. Therefore, the request should only contain the
        properties of the attributes object that need to be updated.

        The request must include an "application/merge-patch+json" content-type header.

        :param object_id: Object record ID
        :param data: Object record
        :return: Updated object record
        """

        self._session.headers['Content-type'] = 'application/merge-patch+json'
        return self._session.patch(f'{self._objects_base_url}/records/{object_id}', json=data)

    def update_by_external_id(self, data: dict) -> Response:
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

        self._session.headers['Content-type'] = 'application/merge-patch+json'
        return self._session.patch(f'{self._objects_base_url}/records', json=data)

    def delete(self, object_id: str) -> Response:
        """
        Deletes the specified object record.

        Before deleting an object record, you must delete any relationship record that specifies the object record

        :param object_id: Object record ID
        :return: Nothing
        """

        return self._session.delete(f'{self._objects_base_url}/records/{object_id}')
