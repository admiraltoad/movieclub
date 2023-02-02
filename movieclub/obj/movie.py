from movieclub.framework.rest_object import RestObject

class Movie(RestObject):
    def get_credits(self):
        """Gets the cast and crew credits for the current movie."""
        return self._rest_api.get(f"movie/{self._data['id']}/credits")

    def get_keywords(self):
        """Gets the keywords associated with the current movie."""
        return self._rest_api.get(f"movie/{self._data['id']}/keywords").get("keywords", [])
