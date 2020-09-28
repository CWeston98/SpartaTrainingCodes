import requests
from pprint import pprint


class Berries:
    def __init__(self, name, url):
        self.name = name
        self.link = url
        self.info = self._get_info()

    def _berry_lookup(self):
        req_response = requests.get(self.link)
        response = req_response.json()
        berry_dict = {}
        for berry_detail in response:
            if berry_detail:
                berry_dict[berry_detail] = response[berry_detail]
        return berry_dict

    def _firmness(self):
        full_dict = self._berry_lookup()
        return {"Firmness": full_dict['firmness']['name']}

    def _flavour(self):
        full_dict = self._berry_lookup()
        berry_flavour = full_dict['flavors']
        new_list = []
        for index in range(0, len(berry_flavour)):
            current_berry = {}
            current_berry['Flavour'] = berry_flavour[index]['flavor']['name']
            current_berry['Potency'] = berry_flavour[index]['potency']
            new_list.append(current_berry)
        return new_list

    def _natural_gift(self):
        full_dict = self._berry_lookup()
        new_dict = {
            'Type': full_dict['natural_gift_type']['name'],
            'Power': full_dict['natural_gift_power']
        }
        return {'Natural Gift': new_dict}

    def _misc(self):
        full_dict = self._berry_lookup()
        new_dict = {
            'Size': full_dict['size'],
            'Smoothness': full_dict['smoothness'],
            'Soil Dryness': full_dict['soil_dryness'],
            'Growth Time': full_dict['growth_time']
        }
        return {"Misc Info": new_dict}

    def _get_info(self):
        info = [self._firmness(), self._flavour(), self._natural_gift(), self._misc()]
        return info