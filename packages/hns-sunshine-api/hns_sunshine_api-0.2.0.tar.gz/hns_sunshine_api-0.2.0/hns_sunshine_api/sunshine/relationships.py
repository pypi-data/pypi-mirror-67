from hns_sunshine_api.sunshine.base import SunshineBase


class SunshineRelationships(SunshineBase):
    """ Sunshine relationships class """

    def __init__(self, subdomain: str, email: str, key: str):
        super().__init__(subdomain, email, key)

    def __repr__(self):
        return f'SunshineRelationships(subdomain="{self.subdomain}")'

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

