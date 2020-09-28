import requests
from pprint import pprint


class BerryFlavour:
    def __init__(self, flavour, url):
        self.flavour = flavour
        self.link = url
        self.info = self._get_info()

    def _lookup(self):
        req_response = requests.get(self.link)
        response = req_response.json()
        lookup_dict = {}
        for detail in response:
            if detail:
                lookup_dict[detail] = response[detail]
        return lookup_dict

    def _find_berry(self):
        full_dict = self._lookup()
        berries = full_dict['berries']
        berry_list = []
        for index in range(0, len(berries)):
            current_dict = {
                'Name': berries[index]['berry']['name'],
                'Potency': berries[index]['potency']
            }
            berry_list.append(current_dict)
        return berry_list

    def _contest_type(self):
        full_dict = self._lookup()
        return {'Contest Type': full_dict['contest_type']['name']}

    def _get_info(self):
        return[self._contest_type(), self._find_berry()]
