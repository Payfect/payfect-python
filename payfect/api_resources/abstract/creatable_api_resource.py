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

        return r.json()
