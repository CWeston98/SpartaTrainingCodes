import requests


class ContentModel:
    def __init__(self, dictionary, page):
        self.all = dictionary
        self.import_info = ['characteristic', 'contest_effect', 'evolution_chain', 'machine', 'super_contest_effect']
        self.no_add_info = ['berry_firmness', 'encounter_condition']
        self.ready = ['ability', 'berry', 'berry_flavour', 'contest_type', 'egg_group', 'pokemon']
        if page == 'homepage_url':
            self.ability = dictionary['ability']
            self.berry = dictionary['berry']
            self.berry_firmness = dictionary['berry-firmness']
            self.berry_flavour = dictionary['berry-flavor']
            self.characteristic = dictionary['characteristic']
            self.contest_effect = dictionary['contest-effect']
            self.contest_type = dictionary['contest-type']
            self.egg_group = dictionary['egg-group']
            self.encounter_condition = dictionary['encounter-condition']
            self.encounter_condition_value = dictionary['encounter-condition-value']
            self.encounter_method = dictionary['encounter-method']
            self.evolution_chain = dictionary['evolution-chain']
            self.evolution_trigger = dictionary['evolution-trigger']
            self.gender = dictionary['gender']
            self.generation = dictionary['generation']
            self.growth_rate = dictionary['growth-rate']
            self.item = dictionary['item']
            self.item_attribute = dictionary['item-attribute']
            self.item_category = dictionary['item-category']
            self.item_fling_effect = dictionary['item-fling-effect']
            self.item_pocket = dictionary['item-pocket']
            self.language = dictionary['language']
            self.location = dictionary['location']
            self.location_area = dictionary['location-area']
            self.machine = dictionary['machine']
            self.move = dictionary['move']
            self.move_ailment = dictionary['move-ailment']
            self.move_battle_style = dictionary['move-battle-style']
            self.move_category = dictionary['move-category']
            self.move_damage_class = dictionary['move-damage-class']
            self.move_learn_method = dictionary['move-learn-method']
            self.move_target = dictionary['move-target']
            self.nature = dictionary['nature']
            self.pal_park_area = dictionary['pal-park-area']
            self.pokeathlon_stat = dictionary['pokeathlon-stat']
            self.pokedex = dictionary['pokedex']
            self.pokemon = dictionary['pokemon']
            self.pokemon_colour = dictionary['pokemon-color']
            self.pokemon_form = dictionary['pokemon-form']
            self.pokemon_habitat = dictionary['pokemon-habitat']
            self.pokemon_shape = dictionary['pokemon-shape']
            self.pokemon_species = dictionary['pokemon-species']
            self.pokemon_region = dictionary['region']
            self.pokemon_stat = dictionary['stat']
            self.super_contest_effect = dictionary['super-contest-effect']
            self.type = dictionary['type']
            self.version = dictionary['version']
            self.version_group = dictionary['version-group']
        else:
            self.count = dictionary['count']
            self.results = dictionary['results']
            if page in self.ready:
                self.dict = {}
                page_list = []
                page_link = []
                for each in self.results:
                    page_list.append(each['name'])
                    page_link.append(each['url'])
                self.sorted_list = sorted(page_list)
                for number in range(0, self.count):
                    self.dict[page_list[number]] = page_link[number]
                    self.more_info = True
            elif page == 'berry_firmness':
                berry_firmness_list = []
                for each in self.results:
                    berry_firmness_list.append(each['name'])
                self.sorted_list = sorted(berry_firmness_list)
                self.dict = {'Firmness': self.sorted_list}
                self.more_info = False
            elif page == 'encounter_condition':
                self.dict = {}
                encounter_condition_list = []
                for each in self.results:
                    encounter_condition_list.append(each['name'])
                self.sorted_list = sorted(encounter_condition_list)
                self.dict = {'Encounter Types': self.sorted_list}
                self.more_info = False
            elif page == 'encounter_method':
                self.dict = {}
                encounter_method_list = []
                encounter_method_link = []
                for each in self.results:
                    encounter_method_list.append(each['name'])
                    encounter_method_link.append(each['url'])
                self.sorted_list = sorted(encounter_method_list)
                for number in range(0, self.count):
                    self.dict[encounter_method_list[number]] = encounter_method_link[number]
            elif page == 'evolution_trigger':
                self.dict = {}
                evolution_trigger_list = []
                evolution_trigger_link = []
                for each in self.results:
                    evolution_trigger_list.append(each['name'])
                    evolution_trigger_link.append(each['url'])
                self.sorted_list = sorted(evolution_trigger_list)
                for number in range(0, self.count):
                    self.dict[evolution_trigger_list[number]] = evolution_trigger_link[number]
            elif page == 'gender':
                self.dict = {}
                gender_list = []
                gender_link = []
                for each in self.results:
                    gender_list.append(each['name'])
                    gender_link.append(each['url'])
                self.sorted_list = sorted(gender_list)
                for number in range(0, self.count):
                    self.dict[gender_list[number]] = gender_link[number]
            elif page == 'generation':
                self.dict = {}
                generation_list = []
                generation_link = []
                for each in self.results:
                    generation_list.append(each['name'])
                    generation_link.append(each['url'])
                self.sorted_list = sorted(generation_list)
                for number in range(0, self.count):
                    self.dict[generation_list[number]] = generation_link[number]
            elif page == 'growth_rate':
                self.dict = {}
                growth_rate_list = []
                growth_rate_link = []
                for each in self.results:
                    growth_rate_list.append(each['name'])
                    growth_rate_link.append(each['url'])
                self.sorted_list = sorted(growth_rate_list)
                for number in range(0, self.count):
                    self.dict[growth_rate_list[number]] = growth_rate_link[number]
            elif page == 'item':
                self.dict = {}
                item_list = []
                item_link = []
                for each in self.results:
                    item_list.append(each['name'])
                    item_link.append(each['url'])
                self.sorted_list = sorted(item_list)
                for number in range(0, self.count):
                    self.dict[item_list[number]] = item_link[number]
            elif page == 'item_attribute':
                self.dict = {}
                item_attribute_list = []
                item_attribute_link = []
                for each in self.results:
                    item_attribute_list.append(each['name'])
                    item_attribute_link.append(each['url'])
                self.sorted_list = sorted(item_attribute_list)
                for number in range(0, self.count):
                    self.dict[item_attribute_list[number]] = item_attribute_link[number]
            elif page == 'item_category':
                self.dict = {}
                item_category_list = []
                item_category_link = []
                for each in self.results:
                    item_category_list.append(each['name'])
                    item_category_link.append(each['url'])
                self.sorted_list = sorted(item_category_list)
                for number in range(0, self.count):
                    self.dict[item_category_list[number]] = item_category_link[number]
            elif page == 'item_fling_effect':
                self.dict = {}
                item_fling_effect_list = []
                item_fling_effect_link = []
                for each in self.results:
                    item_fling_effect_list.append(each['name'])
                    item_fling_effect_link.append(each['url'])
                self.sorted_list = sorted(item_fling_effect_list)
                for number in range(0, self.count):
                    self.dict[item_fling_effect_list[number]] = item_fling_effect_link[number]
            elif page == 'item_pocket':
                self.dict = {}
                item_pocket_list = []
                item_pocket_link = []
                for each in self.results:
                    item_pocket_list.append(each['name'])
                    item_pocket_link.append(each['url'])
                self.sorted_list = sorted(item_pocket_list)
                for number in range(0, self.count):
                    self.dict[item_pocket_list[number]] = item_pocket_link[number]
            elif page == 'language':
                self.dict = {}
                language_list = []
                language_link = []
                for each in self.results:
                    language_list.append(each['name'])
                    language_link.append(each['url'])
                self.sorted_list = sorted(language_list)
                for number in range(0, self.count):
                    self.dict[language_list[number]] = language_link[number]
            elif page == 'location':
                self.dict = {}
                location_list = []
                location_link = []
                for each in self.results:
                    location_list.append(each['name'])
                    location_link.append(each['url'])
                self.sorted_list = sorted(location_list)
                for number in range(0, self.count):
                    self.dict[location_list[number]] = location_link[number]
            elif page == 'location_area':
                self.dict = {}
                location_area_list = []
                location_area_link = []
                for each in self.results:
                    location_area_list.append(each['name'])
                    location_area_link.append(each['url'])
                self.sorted_list = sorted(location_area_list)
                for number in range(0, self.count):
                    self.dict[location_area_list[number]] = location_area_link[number]
            elif page == 'move':
                self.dict = {}
                move_list = []
                move_link = []
                for each in self.results:
                    move_list.append(each['name'])
                    move_link.append(each['url'])
                self.sorted_list = sorted(move_list)
                for number in range(0, self.count):
                    self.dict[move_list[number]] = move_link[number]
            elif page == 'move_ailment':
                self.dict = {}
                move_ailment_list = []
                move_ailment_link = []
                for each in self.results:
                    move_ailment_list.append(each['name'])
                    move_ailment_link.append(each['url'])
                self.sorted_list = sorted(move_ailment_list)
                for number in range(0, self.count):
                    self.dict[move_ailment_list[number]] = move_ailment_link[number]
            elif page == 'move_battle_style':
                self.move_battle_style_dict = {}
                move_battle_style_list = []
                move_battle_style_link = []
                for each in self.results:
                    move_battle_style_list.append(each['name'])
                    move_battle_style_link.append(each['url'])
                self.sorted_list = sorted(move_battle_style_list)
                for number in range(0, self.count):
                    self.dict[move_battle_style_list[number]] = move_battle_style_link[number]
            elif page == 'move_learn_method':
                self.dict = {}
                move_learn_method_list = []
                move_learn_method_link = []
                for each in self.results:
                    move_learn_method_list.append(each['name'])
                    move_learn_method_link.append(each['url'])
                self.sorted_list = sorted(move_learn_method_list)
                for number in range(0, self.count):
                    self.dict[move_learn_method_list[number]] = move_learn_method_link[number]
            elif page == 'move_target':
                self.dict = {}
                move_target_list = []
                move_target_link = []
                for each in self.results:
                    move_target_list.append(each['name'])
                    move_target_link.append(each['url'])
                self.sorted_list = sorted(move_target_list)
                for number in range(0, self.count):
                    self.dict[move_target_list[number]] = move_target_link[number]
            elif page == 'nature':
                self.dict = {}
                nature_list = []
                nature_link = []
                for each in self.results:
                    nature_list.append(each['name'])
                    nature_link.append(each['url'])
                self.sorted_list = sorted(nature_list)
                for number in range(0, self.count):
                    self.dict[nature_list[number]] = nature_link[number]
            elif page == 'pal_park_area':
                self.dict = {}
                pal_park_area_list = []
                pal_park_area_link = []
                for each in self.results:
                    pal_park_area_list.append(each['name'])
                    pal_park_area_link.append(each['url'])
                self.sorted_list = sorted(pal_park_area_list)
                for number in range(0, self.count):
                    self.dict[pal_park_area_list[number]] = pal_park_area_link[number]
            elif page == 'pokeathlon_stat':
                self.dict = {}
                pokeathlon_stat_list = []
                pokeathlon_stat_link = []
                for each in self.results:
                    pokeathlon_stat_list.append(each['name'])
                    pokeathlon_stat_link.append(each['url'])
                self.sorted_list = sorted(pokeathlon_stat_list)
                for number in range(0, self.count):
                    self.dict[pokeathlon_stat_list[number]] = pokeathlon_stat_link[number]
            elif page == 'pokedex':
                self.dict = {}
                pokedex_list = []
                pokedex_link = []
                for each in self.results:
                    pokedex_list.append(each['name'])
                    pokedex_link.append(each['url'])
                self.sorted_list = sorted(pokedex_list)
                for number in range(0, self.count):
                    self.dict[pokedex_list[number]] = pokedex_link[number]
            elif page == 'pokemon_colour':
                self.dict = {}
                pokemon_colour_list = []
                pokemon_colour_link = []
                for each in self.results:
                    pokemon_colour_list.append(each['name'])
                    pokemon_colour_link.append(each['url'])
                self.sorted_list = sorted(pokemon_colour_list)
                for number in range(0, self.count):
                    self.dict[pokemon_colour_list[number]] = pokemon_colour_link[number]
            elif page == 'pokemon_form':
                self.dict = {}
                pokemon_form_list = []
                pokemon_form_link = []
                for each in self.results:
                    pokemon_form_list.append(each['name'])
                    pokemon_form_link.append(each['url'])
                self.sorted_list = sorted(pokemon_form_list)
                for number in range(0, self.count):
                    self.dict[pokemon_form_list[number]] = pokemon_form_link[number]
            elif page == 'pokemon_habitat':
                self.dict = {}
                pokemon_habitat_list = []
                pokemon_habitat_link = []
                for each in self.results:
                    pokemon_habitat_list.append(each['name'])
                    pokemon_habitat_link.append(each['url'])
                self.sorted_list = sorted(pokemon_habitat_list)
                for number in range(0, self.count):
                    self.dict[pokemon_habitat_list[number]] = pokemon_habitat_link[number]
            elif page == 'pokemon_shape':
                self.dict = {}
                pokemon_shape_list = []
                pokemon_shape_link = []
                for each in self.results:
                    pokemon_shape_list.append(each['name'])
                    pokemon_shape_link.append(each['url'])
                self.sorted_list = sorted(pokemon_shape_list)
                for number in range(0, self.count):
                    self.dict[pokemon_shape_list[number]] = pokemon_shape_link[number]
            elif page == 'pokemon_species':
                self.dict = {}
                pokemon_species_list = []
                pokemon_species_link = []
                for each in self.results:
                    pokemon_species_list.append(each['name'])
                    pokemon_species_link.append(each['url'])
                self.sorted_list = sorted(pokemon_species_list)
                for number in range(0, self.count):
                    self.dict[pokemon_species_list[number]] = pokemon_species_link[number]
            elif page == 'region':
                self.dict = {}
                region_list = []
                region_link = []
                for each in self.results:
                    region_list.append(each['name'])
                    region_link.append(each['url'])
                self.sorted_list = sorted(region_list)
                for number in range(0, self.count):
                    self.dict[region_list[number]] = region_link[number]
            elif page == 'stat':
                self.dict = {}
                stat_list = []
                stat_link = []
                for each in self.results:
                    stat_list.append(each['name'])
                    stat_link.append(each['url'])
                self.sorted_list = sorted(stat_list)
                for number in range(0, self.count):
                    self.dict[stat_list[number]] = stat_link[number]
            elif page == 'type':
                self.dict = {}
                type_list = []
                type_link = []
                for each in self.results:
                    type_list.append(each['name'])
                    type_link.append(each['url'])
                self.sorted_list = sorted(type_list)
                for number in range(0, self.count):
                    self.dict[type_list[number]] = type_link[number]
            elif page == 'version':
                self.dict = {}
                version_list = []
                version_link = []
                for each in self.results:
                    version_list.append(each['name'])
                    version_link.append(each['url'])
                self.sorted_list = sorted(version_list)
                for number in range(0, self.count):
                    self.dict[version_list[number]] = version_link[number]
            elif page == 'version_group':
                self.dict = {}
                version_group_list = []
                version_group_link = []
                for each in self.results:
                    version_group_list.append(each['name'])
                    version_group_link.append(each['url'])
                self.sorted_list = sorted(version_group_list)
                for number in range(0, self.count):
                    self.dict[version_group_list[number]] = version_group_link[number]
            # These had no names in overview page
            elif page == 'characteristic':
                self.dict = {}
                self.sorted_list = []
                for number in range(0, self.count):
                    self.dict[number + 1] = self.results[number]['url']
                    self.sorted_list.append(number + 1)
            elif page == 'contest_effect':
                self.sorted_list = []
                self.dict = {}
                for number in range(0, self.count):
                    self.dict[number + 1] = self.results[number]['url']
                    self.sorted_list.append(number + 1)
            elif page == 'evolution_chain':
                self.sorted_list = []
                self.dict = {}
                for number in range(0, self.count):
                    self.dict[number + 1] = self.results[number]['url']
                    self.sorted_list.append(number + 1)
            elif page == 'machine':
                self.sorted_list = []
                self.dict = {}
                for number in range(0, self.count):
                    self.dict[number + 1] = self.results[number]['url']
                    self.sorted_list.append(number + 1)
            elif page == 'super_contest_effect':
                self.sorted_list = []
                self.dict = {}
                for number in range(0, self.count):
                    self.dict[number + 1] = self.results[number]['url']
                    self.sorted_list.append(number + 1)

    def lookup(self):
        req_response = requests.get(self.link)
        response = req_response.json()
        lookup_dict = {}
        for detail in response:
            if detail:
                lookup_dict[detail] = response[detail]
        return lookup_dict



