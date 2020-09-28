from population_model.solo_rabbit_project.config.config_manager import find_var_hawk
import ast
from population_model.solo_rabbit_project.classes.animal import Animal
import random as rd
import math


class Hawk(Animal):
    def __init__(self):
        super().__init__()
        self.population = 0
        self.starting_month = int(find_var_hawk('month_introduced'))
        self.per_birth = [int(find_var_hawk('babies_min')), int(find_var_hawk('babies_max'))]
        self.death_age = int(find_var_hawk('death_age'))
        self.maturity = int(find_var_hawk('maturity'))
        self.rabbits_eaten = int(find_var_hawk('rabbits_eaten'))
        self.starved = 0

    def intro_hawks(self):
        # Sets the initial conditions for the hawk population
        self.generation_dict = ast.literal_eval(find_var_hawk('hawks_introduced'))
        for each in range(0, int(find_var_hawk('months_between_breeding'))):
            self.pregnancies.append(0)
        for generation in self.generation_dict:
            self.males += self.generation_dict[generation]['Males']
            self.females += self.generation_dict[generation]['Females']
        self.population = self.males + self.females

    def eat_rabbits(self):
        # Finds the amount of rabbits eaten
        return self.population * self.rabbits_eaten

    def starving(self, rabbits_short):
        # Determines which hawks will starve
        if rabbits_short != 0:
            hawks_left = math.ceil(rabbits_short/self.rabbits_eaten)
            self.starved += hawks_left
            while hawks_left > 0:
                gender = ['Males', 'Females'][rd.randint(0, 1)]
                hawk_ages = list(self.generation_dict.keys())  # Finding the ages for which there are hawks
                age = rd.choice(hawk_ages)
                if self.generation_dict[age][gender] > 0:
                    self.generation_dict[age][gender] -= 1
                    hawk_ages -= 1
                elif self.generation_dict[age]['Males'] == 0 and self.generation_dict[age]['Females'] == 0:
                    del self.generation_dict[age]  # Deleting excess key-value pairs
