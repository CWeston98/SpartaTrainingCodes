from classes.animal import Animal


def test_assign_gender():
    test_object = Animal()
    test_object.births = 20
    test_object.assign_gender()
    boys = test_object.generation_dict[0]['Males']
    girls = test_object.generation_dict[0]['Females']
    assert 0 <= boys <= 20
    assert 0 <= girls <= 20
    assert boys + girls == 20
    test_object.births = 0
    test_object.assign_gender()
    assert test_object.generation_dict[0]['Males'] == 0
    assert test_object.generation_dict[0]['Females'] == 0


test_assign_gender()