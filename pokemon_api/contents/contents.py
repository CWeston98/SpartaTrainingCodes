import requests
from pokemon_api.contents.contents_model import ContentModel
from pokemon_api.contents.config_manager import find_url
from pprint import pprint


class ContentPage:
    def __init__(self, page=None, specific=None):
        if not page:
            page = input('Which page would you like to look at?\n')
        self.url = find_url(page.lower())
        print(self.url)
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.contents_dict = self._delete_page_refs()
        self.page_name = page.lower()
        self.specific = specific
        self.info = self._get_info()

    def _delete_page_refs(self):
        # Removes superfluous entries in the dictionary
        dictionary = self.request.json()
        for each in ['next', 'previous']:
            if each in dictionary:
                del dictionary[each]
        return dictionary

    def _response(self):
        # Finds the corresponding URL and list of subclasses using the model
        return ContentModel(self.contents_dict, self.page_name)

    def _use_contents(self):
        # Prints list of subclasses and asks which one to go to
        if self._response().more_info:
            pprint(self._response().sorted_list)
            if self.specific:
                self.specific = self.specific.lower()
            else:
                self.specific = input(f'Which {self.page_name} would you like to look at?\n').lower()
            try:
                new_page = self._response().dict[self.specific]
                return new_page
            except KeyError:
                print(f'There is no {self.page_name} with that name')
        else:
            pprint(self._response().dict)

    def _get_info(self):
        # Looks up info using the associated class
        link = self._use_contents()
        if self.specific:
            if self.page_name == 'ability':
                from pokemon_api.pages.get_ability import Abilities
                ability = Abilities(self.specific, link)
                ability.write_to_file()
                return ability.info
            elif self.page_name == 'berry':
                from pokemon_api.pages.get_berry import Berries
                return Berries(self.specific, link).info
            elif self.page_name == 'berry_flavour':
                from pokemon_api.pages.get_berry_flavour import BerryFlavour
                return BerryFlavour(self.specific, link).info
            elif self.page_name == 'contest_type':
                from pokemon_api.pages.get_contest_type import ContestTypes
                return ContestTypes(self.specific, link).info
            elif self.page_name == 'egg_group':
                from pokemon_api.pages.get_egg_group import EggGroups
                return EggGroups(self.specific, link).info
            elif self.page_name == 'pokemon':
                from pokemon_api.pages.get_pokemon import Pokemon
                pokemon = Pokemon(self.specific, link)
                pokemon.write_to_file()
                return pokemon.info
        else:
            return 'No further information available'


info = ContentPage()
