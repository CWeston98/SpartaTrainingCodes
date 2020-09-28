from classes.animal import Animal


def test_find_populations():
    test_object = Animal()
    test_object.generation_dict[5] = {'Males': 3, 'Females': 1}
    test_object.find_population()
    assert test_object.males == 3
    assert test_object.females == 1
    assert test_object.population == 4
    test_object.generation_dict[7] = {'Males': 2, 'Females': 1}
    test_object.find_population()
    assert test_object.males == 5
    assert test_object.females == 2
    assert test_object.population == 7


test_find_populations()
