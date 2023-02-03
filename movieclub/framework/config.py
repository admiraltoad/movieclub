import yaml
class Config:
    def __init__(self, filepath):
        """Configuration file used to store user credentials."""
        with open(filepath, "r") as config:
            self._data = yaml.load(config, Loader=yaml.Loader)
    @property
    def api_key(self):
        return self._data.get("api_key")
    @property
    def user_token(self):
        return self._data.get("user_token")
    @property
    def username(self):
        return self._data.get("username")
    @property
    def password(self):
        return self._data.get("password")