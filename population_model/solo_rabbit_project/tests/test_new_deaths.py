from classes.rabbit import Rabbit


def test_new_deaths():
    test_object = Rabbit()
    test_object.generation_dict[test_object.death_age] = {'Males': 2, 'Females': 1}
    test_object.new_deaths()
    assert test_object.deaths['Males'] == 2
    assert test_object.deaths['Females'] == 1
    test_object.generation_dict[60] = {'Males': 2, 'Females': 0}
    test_object.new_deaths()
    assert test_object.deaths['Males'] == 4
    assert test_object.deaths['Females'] == 1
    test_object.find_population()
    assert test_object.population == 2
    assert test_object.males == 1


test_new_deaths()
