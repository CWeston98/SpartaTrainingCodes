import requests


class ContestTypes:
    def __init__(self, c_type, url):
        self.c_type = c_type
        self.link = url
        self.info = self._find_berry()

    def _type_lookup(self):
        req_response = requests.get(self.link)
        response = req_response.json()
        type_dict = {}
        for type_detail in response:
            if type_detail:
                type_dict[type_detail] = response[type_detail]
        return type_dict

    def _find_berry(self):
        full_dict = self._type_lookup()
        berry_flavour = full_dict['berry_flavor']['name']
        return {'Berry Flavour': berry_flavour}
