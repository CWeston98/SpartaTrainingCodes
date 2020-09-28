from classes.rabbit import Rabbit


def test_new_pregnancies():
    test_object = Rabbit()
    test_object.new_pregnancies()
    assert test_object.pregnancies[2] == 1
    test_object.population[5] = {'Males': 3, 'Females': 2}
    test_object.new_pregnancies()
    assert test_object.pregnancies[3] == 2
    assert test_object.pregnancies[2] == 1


test_new_pregnancies()