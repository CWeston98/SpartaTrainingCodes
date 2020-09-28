import requests


class Abilities:
    def __init__(self, ability, url):
        self.ability = ability
        self.link = url
        self.info = self._get_info()

    def _ability_lookup(self):
        req_response = requests.get(self.link)
        response = req_response.json()
        ability_dict = {}
        for ability_detail in response:
            if ability_detail:
                ability_dict[ability_detail] = response[ability_detail]
        return ability_dict

    def _effect_changes(self):
        full_dict = self._ability_lookup()
        new_dict = {}
        if full_dict['effect_changes']:
            effect_entries = full_dict['effect_changes'][0]['effect_entries']
            version_group = full_dict['effect_changes'][0]['version_group']
            for each in range(0, len(effect_entries)):
                if effect_entries[each]['language']['name'] == 'en':
                    new_dict['Effect Entry'] = effect_entries[each]['effect']
            new_dict['Version Group'] = version_group['name']
            return {"Effect Changes": new_dict}
        else:
            return "No Effect Changes"

    def _effect_entries(self):
        full_dict = self._ability_lookup()
        new_dict = {}
        effects = full_dict['effect_entries']
        for index in range(0, len(effects)):
            if effects[index]['language']['name'] == 'en':
                new_dict['Long Effect'] = effects[index]['effect']
                new_dict['Short Effect'] = effects[index]['short_effect']
        return {"Effect Entries": new_dict}

    def _flavour_text(self):
        full_dict = self._ability_lookup()
        entry_list = []
        flavour_text_entries = full_dict['flavor_text_entries']
        for index in range(0, len(flavour_text_entries)):
            current_dict = {}
            if flavour_text_entries[index]['language']['name'] == 'en':
                current_dict['Version Group'] = flavour_text_entries[index]['version_group']['name']
                current_dict['Text'] = flavour_text_entries[index]['flavor_text']
                entry_list.append(current_dict)
        new_dict = {'Flavour Text': entry_list}
        return new_dict

    def _generation(self):
        full_dict = self._ability_lookup()
        return {"Generation": full_dict['generation']['name']}

    def _pokemon(self):
        full_dict = self._ability_lookup()
        poke_entries = full_dict['pokemon']
        entry_list = []
        for index in range(0, len(poke_entries)):
            if poke_entries[index]['is_hidden']:
                poke_entries[index]['pokemon']['name'] += ' (Hidden)'
            entry_list.append(poke_entries[index]['pokemon']['name'])
        return {'Pokemon': entry_list}

    def _get_info(self):
        info = [self._effect_changes(), self._effect_entries(), self._flavour_text(), self._generation(),
                self._pokemon()]
        return info

    def write_to_file(self):
        pokemon_list = (sorted(self._pokemon()['Pokemon']))
        for index in range (0, len(pokemon_list)):
            pokemon_list[index] = pokemon_list[index].capitalize()
        pokemon_list = "\n   -".join(pokemon_list)
        generation = self._generation()['Generation']
        with open(f'{self.ability} info'.capitalize(), 'w') as opened_file:
            opened_file.write(f"{self.ability.capitalize()} was introduced in {generation}\n\
It can be learned by:\n\n\
   -{pokemon_list}")
