import requests
import urllib.parse

class RestAPI:
    def __init__(self, base_url, api_token):
        """Base implimentation of a Rest API."""
        self._base_url = base_url
        self._api_token = api_token

    def get(self, url, params=None):
        """"""
        url_params = urllib.parse.urlencode(params) if params else ""
        resp = requests.get(f"{self._base_url}{url}?api_key={self._api_token}&language=en-US&{url_params}")
        resp.raise_for_status()
        return resp.json()
