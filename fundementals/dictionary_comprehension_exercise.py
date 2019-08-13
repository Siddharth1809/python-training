# create dictionary from two lists
def create_dict():
    names = ['abc', 'mno', 'pqr', 'xyz']
    roll = [1, 2, 3, 4]
    my_dict = dict(zip(names, roll))
    print(my_dict)


create_dict()


# create dictionary using comprehension
def create_dict_comprehension():
    names = ['abc', 'mno', 'pqr', 'xyz']
    roll = [1, 2, 3, 4]
    my_dict = {names: roll for names, roll in zip(names, roll)}
    print(my_dict)


create_dict_comprehension()


# if name is not equal to pqr then print my_dict
def edit_dict_comprehension():
    names = ['abc', 'mno', 'pqr', 'xyz']
    roll = [1, 2, 3, 4]
    my_dict = {names: roll for names, roll in zip(names, roll) if names != 'pqr'}
    print("Dictionary without key:'pqr':", my_dict)


edit_dict_comprehension()


def mul_dict_val():
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    result = {key: value * 2 for key, value in dict1.items()}
    print("original dict:", dict1)
    print("After double the value of dict1:", result)


mul_dict_val()


def dictionary_func():
    temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = {i: i ** 2 for i in temp}
    print("My new dictionary:", result)


dictionary_func()


def dictionary_func_even():
    temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = {i: i ** 2 for i in temp if i % 2 == 0}
    print("My new dictionary:", result)


dictionary_func_even()


def swap_key_value():
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    dict2 = {}
    for key, val in dict1.items():
        dict2[val] = key
    print("Actual dictionary", dict1)
    print("After swapping key and values in dict1:", dict2)


swap_key_value()
