import requests
from starwars_mongodb.config.config_manager import find_def_var
from starwars_mongodb.config.config_manager import find_star_var


class Starships:
    def __init__(self):
        self.home = str(find_def_var("home") + find_star_var("extension"))
        self.page_links = []
        self.starships = {}
        self._get_links()
        self._get_requests()

    def _get_links(self):
        # Finds the links for all pages of starships
        for number in range(1, 1 + int(find_star_var("number_of_pages"))):
            self.page_links.append(self.home + str(number))

    def _get_requests(self):
        # Adds all starship info to a dictionary; key is starship name
        for page in self.page_links:
            info = requests.get(page).json()
            for starship in info['results']:
                name = starship['name']
                self.starships[name] = starship

    def _get_cats(self, starship):
        # Adds info for the starship-specific categories
        wanted_info = {}
        info = self.starships[starship]

        # Saves info for categories that would be strings
        for category in find_star_var('str_cats'):
            # if category != 'unknown' and category != 'n/a':
            wanted_info[category] = info[category]

        # Saves info for categories that would be ints
        for category in find_star_var("int_cats"):
            if "," in info[category]:
                info[category] = info[category].replace(",", "")
            if "km" in info[category]:
                info[category] = info[category].replace("km", "")
            try:
                wanted_info[category] = int(info[category])
            except ValueError:
                # Would be where I update category with n/a and unknown values if wanted
                "do nothing"

        # Saves info for categories that would be floats
        for category in find_star_var('float_cats'):
            if "," in info[category]:
                info[category] = info[category].replace(",", "")
            try:
                wanted_info[category] = float(info[category])
            except ValueError:
                # Would be where I update category with unknown values if wanted
                "do nothing"

        return wanted_info
