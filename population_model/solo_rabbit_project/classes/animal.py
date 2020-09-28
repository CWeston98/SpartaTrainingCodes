from random import randint
import numpy as np


class Animal:
    def __init__(self):
        self.population = 0
        self.males = 0
        self.females = 0
        self.pregnancies = []
        self.births = 0
        self.maturity = 0
        self.generation_dict = {}
        self.death_age = 0
        self.deaths = {'Males': 0, 'Females': 0}

    def new_pregnancies(self):
        # Calculates the number of each animal that will get pregnant
        mature_males = 0
        mature_females = 0
        for generation in self.generation_dict:  # Finds number of mature males/females
            if int(generation) >= self.maturity:
                mature_males += self.generation_dict[generation]['Males']
                mature_females += self.generation_dict[generation]['Females']
        currently_pregnant = sum(self.pregnancies)  # Finds number of animal pregnant at start of the month
        self.pregnancies.append(min(mature_males, mature_females - currently_pregnant))

    def give_birth(self, minimum, maximum):
        # Calculates the number of babies born
        birthing_animals = self.pregnancies.pop(0)  # Allows rabbits to give birth
        if birthing_animals > 500:
            avg = (self.per_birth[0] + self.per_birth[1])/2
            sigma = birthing_animals**(-0.5)
            per_birth = np.random.normal(loc=avg, scale=sigma)
            new_babies = round(birthing_animals * per_birth)
        else:
            new_babies = 0
            for mother in range(0, birthing_animals):
                new_babies += randint(minimum, maximum)
        self.births = new_babies

    def assign_gender(self):
        # Randomly assigns the gender of babies
        if self.births > 500:
            n, p = self.births, 0.5
            baby_boys = np.random.binomial(n, p)
            baby_girls = self.births - baby_boys
        else:
            baby_boys = 0
            baby_girls = 0
            for baby in range(0, self.births):
                gender = ['M', 'F'][randint(0, 1)]
                if gender == 'M':
                    baby_boys += 1
                else:
                    baby_girls += 1
        self.generation_dict[0] = {'Males': baby_boys, 'Females': baby_girls}

    def new_deaths(self):
        # Ensures animals die when they exceed their maximum age
        try:
            dead_males = self.generation_dict[self.death_age]['Males']
            dead_females = self.generation_dict[self.death_age]['Females']
            del self.generation_dict[self.death_age]
        except KeyError:
            dead_males = 0
            dead_females = 0
        self.deaths['Males'] += dead_males
        self.deaths['Females'] += dead_females

    def age_up(self):
        # Ages animals by 1 month
        new_ages = {}
        for generation in self.generation_dict:
            new_ages[generation + 1] = self.generation_dict[generation]
        self.generation_dict = new_ages

    def find_population(self):
        # Calculates the total population of the animal
        males = 0
        females = 0
        for generation in self.generation_dict:
            males += self.generation_dict[generation]['Males']
            females += self.generation_dict[generation]['Females']
        self.males = males
        self.females = females
        self.population = males + females
