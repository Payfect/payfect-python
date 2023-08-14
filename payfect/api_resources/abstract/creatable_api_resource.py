import payfect
import requests

from .api_resource import APIResource


class CreatableAPIResource(APIResource):
    @classmethod
    def create(
        cls,
        **params
    ):
        url = cls.class_url()
        r = requests.post(
            url,
            json=params,
            headers={
                'Authorization': f'Api-Key {payfect.api_key}'
            }
        )

        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception(r.status_code, r.reason, r.json())

        return r.json()
