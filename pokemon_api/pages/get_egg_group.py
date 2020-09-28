import requests


class EggGroups:
    def __init__(self, group, url):
        self.group = group
        self.link = url
        self.info = self._find_pokemon()

    def _egg_lookup(self):
        req_response = requests.get(self.link)
        response = req_response.json()
        egg_dict = {}
        for egg_detail in response:
            if egg_detail:
                egg_dict[egg_detail] = response[egg_detail]
        return egg_dict

    def _find_pokemon(self):
        full_dict = self._egg_lookup()
        new_list = []
        pokemon = full_dict['pokemon_species']
        for index in range(0, len(pokemon)):
            new_list.append((pokemon[index]['name']))
        new_list = sorted(new_list)
        return {'Pokemon in Group': new_list}
