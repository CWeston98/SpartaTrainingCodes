from population_model.solo_rabbit_project.config.config_manager import find_var_rabbit
import ast
from population_model.solo_rabbit_project.classes.animal import Animal
import random as rd


class Rabbit(Animal):
    def __init__(self):
        super().__init__()
        self.death_age = int(find_var_rabbit('rabbit_death_age'))
        self.maturity = int(find_var_rabbit('rabbit_maturity'))
        self.per_birth = [int(find_var_rabbit('rabbit_babies_min')), int(find_var_rabbit('rabbit_babies_max'))]
        self.eaten = 0
        self.set_init()

    def set_init(self):
        # Sets the initial conditions for the rabbit population
        self.generation_dict = ast.literal_eval(find_var_rabbit('starting_rabbits'))
        for each in range(0, int(find_var_rabbit('months_between_breeding'))):
            self.pregnancies.append(0)
        for generation in self.generation_dict:
            self.males += self.generation_dict[generation]['Males']
            self.females += self.generation_dict[generation]['Females']
        self.population = self.males + self.females

    def get_eaten(self, number):
        # Randomises the rabbits that are eaten
        if number < self.population:
            self.eaten += number
            while number > 0:
                gender = ['Males', 'Females'][rd.randint(0, 1)]
                rabbit_ages = list(self.generation_dict.keys())  # Finding the ages for which there are rabbits
                age = rd.choice(rabbit_ages)
                if self.generation_dict[age][gender] > 0:
                    self.generation_dict[age][gender] -= 1
                    number -= 1
                elif self.generation_dict[age]['Males'] == 0 and self.generation_dict[age]['Females'] == 0:
                    del self.generation_dict[age]
            return 0
        else:
            self.generation_dict = {}
            self.eaten += self.population
            return number - self.population
