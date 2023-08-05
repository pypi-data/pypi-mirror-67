from hns_sunshine_api.sunshine.base import SunshineBase


class SunshineObjects(SunshineBase):
    """ Sunshine Objects class """

    def __init__(self, subdomain: str, email: str, key: str):
        super().__init__(subdomain, email, key)

    def __repr__(self):
        return f'SunshineObjects(subdomain="{self.subdomain}")'

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
