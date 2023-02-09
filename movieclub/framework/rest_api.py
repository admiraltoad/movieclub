import requests
import urllib.parse


class RestAPI:
    def __init__(self, base_url, config):
        """Base implimentation of a Rest API."""
        self._base_url = base_url
        self._config = config

    def get(self, url, params=None, **kwargs):
        """"""
        url_params = urllib.parse.urlencode(params) if params else ""
        resp = requests.get(f"{self._base_url}{url}?api_key={self._config.api_key}&language=en-US&{url_params}",
                            **kwargs)
        resp.raise_for_status()
        return resp.json()
