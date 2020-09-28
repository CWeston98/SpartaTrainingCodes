from starwars_mongodb.starships import Starships
from starwars_mongodb.characters import Characters
import pymongo

db = pymongo.MongoClient()['starwars']


class AddPilots(Starships):
    def __init__(self):
        super().__init__()
        self.chars = Characters()
        self._get_rel_cats()

    def _update_dict(self, link):
        self.chars.url = link
        self.chars.update_char_dict()

    def _get_rel_cats(self):
        for starship in self.starships:
            wanted_info = self._get_cats(starship)
            info = self.starships[starship]

            # Setting the pilots by their memory locations for each starship
            pilot_list = []
            for link in info["pilots"]:
                self._update_dict(link)
                pilot_list.append(self.chars.char_dict[link])
            wanted_info["pilots"] = pilot_list

            # Saving the wanted info for each starship at the end of the iteration
            self.starships[starship] = wanted_info


def add_to_db():
    pilots = AddPilots()
    for starship in pilots.starships:
        db.starships.insert_one(pilots.starships[starship])


add_to_db()
