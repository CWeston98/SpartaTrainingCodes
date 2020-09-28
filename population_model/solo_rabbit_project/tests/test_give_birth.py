from classes.animal import Animal


def test_births():
    test_object = Animal()
    test_object.pregnancies = [1, 3, 0]
    test_object.give_birth(1, 14)
    assert 1 <= test_object.births <= 14
    test_object.give_birth(0, 7)
    assert 0 <= test_object.births <= 21
    test_object.give_birth(1, 3)
    assert test_object.births == 0


test_births()
