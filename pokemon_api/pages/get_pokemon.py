import requests


class Pokemon:
    def __init__(self, name, url):
        self.name = name
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

    def _find_abilities(self):
        full_dict = self._lookup()
        abilities = full_dict['abilities']
        new_list = []
        for index in range(0, len(abilities)):
            if abilities[index]['is_hidden']:
                abilities[index]['ability']['name'] += ' (Hidden)'
            new_list.append(abilities[index]['ability']['name'])
        return {'Abilities': new_list}

    def _find_forms(self):
        full_dict = self._lookup()
        forms = full_dict['forms']
        new_list = []
        for index in range(0, len(forms)):
            new_list.append(forms[index]['name'])
        return {'Forms': new_list}

    def _game_indices(self):
        full_dict = self._lookup()
        games = full_dict['game_indices']
        new_list = []
        for index in range(0, len(games)):
            new_list.append(games[index]['version']['name'])
        return {'Games': new_list}

    def _moves_learned(self):
        full_dict = self._lookup()
        moves = full_dict['moves']
        move_dict = {}
        for index in range(0, len(moves)):
            full_version_dict = {}
            move_name = moves[index]['move']['name']
            for version in range(0, len(moves[index]['version_group_details'])):
                version_dict = {
                    'Level': moves[index]['version_group_details'][version]['level_learned_at'],
                    'How learned': moves[index]['version_group_details'][version]['move_learn_method']['name']
                }
                version_name = moves[index]['version_group_details'][version]['version_group']['name']
                full_version_dict[version_name] = version_dict
            move_dict[move_name] = full_version_dict
        return move_dict

    def _stats(self):
        full_dict = self._lookup()
        stat = full_dict['stats']
        stat_dict = {}
        for index in range(0, len(stat)):
            stat_name = stat[index]['stat']['name']
            stat_score = stat[index]['base_stat']
            stat_dict[stat_name] = stat_score
        return stat_dict

    def _types(self):
        full_dict = self._lookup()
        poke_types = full_dict['types']
        type_list = []
        for index in range(0, len(poke_types)):
            type_list.append(poke_types[index]['type']['name'])
        return type_list

    def _misc(self):
        full_dict = self._lookup()
        height = full_dict['height']
        weight = full_dict['weight']
        xp = full_dict['base_experience']
        misc_dict = {
            'Height': height,
            'Weight': weight,
            'Base XP': xp
        }
        return {'Misc': misc_dict}

    def _get_info(self):
        info = [self._find_abilities(), self._find_forms(), self._game_indices(), self._moves_learned(),
                self._stats(), self._types(), self._misc()]
        return info

    def write_to_file(self):
        types = ", ".join(self._types())
        abilities = " or ".join((self._find_abilities()['Abilities']))
        stats = self._stats()
        stats_list = []
        games = self._game_indices()['Games']
        game_list = '\n   -'.join(games)
        for key in stats:
            stats_list.append(f'{key}: {stats[key]}')
        stats_list = "\n   -".join(stats_list)
        with open(f'{self.name} info'.capitalize(), 'w') as opened_file:
            opened_file.write(f"{self.name} is a(n) {types} type.\n\nIt can have the abilities: {abilities}.\n\
It appears in: \n   -{game_list}\n\
It has a height of {self._misc()['Misc']['Height']} and a weight of {self._misc()['Misc']['Weight']}\n\
Defeating this pokemon yields a base xp of {self._misc()['Misc']['Base XP']}\n\
Additionally it has the following stats:\n\
   -{stats_list}\n\n\n\
   --- For more information, including a list of the moves {self.name} can use, type 'pprint [object_name].info' ---")