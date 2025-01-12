def test_func1():
    name = "john"
    for letter in name:
        assert letter.islower()


def test_check_list_elements():
    list1 = [1, 2, 3, 4]
    list2 = [3, 2, 4, 1]

    for i in range(len(list1)):
        if list1[i] in list2:
            assert True
        else:
            assert False
