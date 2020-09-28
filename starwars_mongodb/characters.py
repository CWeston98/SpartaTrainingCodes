import requests
import pymongo


class Characters:
    def __init__(self):
        super().__init__()
        self.name = ""
        self.characters = pymongo.MongoClient()['starwars'].characters
        self.location = ""
        self.url = ""
        self.char_dict = {}

    def _find_name(self):
        info = requests.get(self.url).json()
        name = info['name']
        self.name = name

    def _find_location(self):
        location = self.characters.find_one({"name": self.name}, {"_id": 1})
        location = location['_id']
        self.location = location

    def update_char_dict(self):
        self._find_name()
        self._find_location()
        self.char_dict[self.url] = self.location
