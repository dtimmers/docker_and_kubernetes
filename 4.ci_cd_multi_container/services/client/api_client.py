import os
import requests


class APIConfig:
    host = os.environ['API_HOST']
    port = os.environ['API_PORT']
    slug_values_all = f'api/values/all'
    slug_indices_all = f'api/indices/all'
    slug_indices_insert = f'api/indices/insert'


class APIClient:

    def __init__(self, api_config: APIConfig):
        self.config = api_config

    def build_url(self, slug: str):
        return f'http://{self.config.host}:{self.config.port}/{slug}'

    def get_all_values(self):
        url = self.build_url(self.config.slug_values_all)

        return requests.get(url).json()

    def get_all_indices(self):
        url = self.build_url(self.config.slug_indices_all)

        return requests.get(url).json()

    def insert_index(self, url_args):
        url = self.build_url(self.config.slug_indices_insert)
        requests.get(url, url_args)
