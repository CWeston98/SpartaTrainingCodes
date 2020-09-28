from time import sleep
from population_model.solo_rabbit_project.classes.rabbit import Rabbit
from population_model.solo_rabbit_project.classes.hawk import Hawk


def run_model():
    month = 0
    year = 0
    rabbit = Rabbit()
    hawk = Hawk()
    while True:
        month += 1
        if month == 12:
            month = 0
            year += 1

        # Progressing rabbits
        rabbit.new_pregnancies()
        rabbit.give_birth(rabbit.per_birth[0], rabbit.per_birth[1])
        rabbit.assign_gender()
        rabbit.age_up()
        rabbit.new_deaths()
        rabbit.find_population()

        # Progressing hawks
        hawk.new_pregnancies()
        hawk.give_birth(hawk.per_birth[0], hawk.per_birth[1])
        hawk.assign_gender()
        hawk.age_up()
        hawk.new_deaths()
        hawk.find_population()
        if month == hawk.starting_month and year == 0:
            hawk.intro_hawks()

        # Hawks eating rabbits
        if month > 6 or year > 0:
            print(1)
            hawk.starving(rabbit.get_eaten(hawk.eat_rabbits()))

        print(f"--- Year: {year}, Month: {month} ---\n")
        print(" - Rabbits - ")
        print(f"Total Population: {rabbit.population} ({rabbit.males} males, {rabbit.females} females)")
        print(f"Natural Deaths: {rabbit.deaths['Males'] + rabbit.deaths['Females']}")
        print(f"Eaten: {rabbit.eaten}\n")

        print(" - Hawks - ")
        print(f"Total Population: {hawk.population} ({hawk.males} males, {hawk.females} females)")
        print(f"Natural Deaths: {hawk.deaths['Males'] + hawk.deaths['Females']}")
        sleep(1)  # Change this to 1 second to get a 1 month/second model
