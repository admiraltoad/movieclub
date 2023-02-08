import click
import requests
import webbrowser
from movieclub.framework.rest_api import RestAPI
from movieclub.obj.movie import Movie
from movieclub.helpers import similar

class UserAccess(RestAPI):
    def __init__(self, config):
        """Used to interact with TheMovieDB Rest API at the User Access level"""
        super().__init__("https://api.themoviedb.org/4/", config)
    def get(self, url, params=None):
        """"""
        headers = {"Authorization": f"Bearer {self._config.user_token}",
                   "Content-Type": "application/json;charset=utf-8"}
        return super().get(url, params, headers=headers)

    def _post(self, url, params=None, **kwargs):
        """"""
        headers = {"Authorization": f"Bearer {self._config.user_token}",
                   "Content-Type": "application/json;charset=utf-8"}
        resp = requests.post(f"{self._base_url}{url}?api_key={self._config.api_key}&language=en-US",
                             headers=headers, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def _create_request_token(self):
        """"""
        data = {"redirect_to": "http://www.themoviedb.org/"}
        return self._post("auth/request_token", data=data).get("request_token")

    def create_session(self):
        """"""
        request_token = self._create_request_token()
        webbrowser.open(f"https://www.themoviedb.org/auth/access?request_token={request_token}")
        if click.prompt("Has authorization been granted?"):
            data = {"request_token": request_token}
            return self._post("auth/access_token", json=data)

    def create_list(self, name):
        """"""
        data = {
            "name": name,
            "iso_639_1": "en"
        }
        return self._post("list", data=data)
