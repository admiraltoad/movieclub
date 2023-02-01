import pprint

class RestObject:
    def __init__(self, rest_api, obj_data):
        """Base implimentation of a Rest Object."""
        self._rest_api = rest_api
        self._data = obj_data

    def __str__(self):
        prettyp = pprint.PrettyPrinter(indent=3)
        return prettyp.pformat(self._data)
