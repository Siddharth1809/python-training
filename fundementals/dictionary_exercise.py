# Various ways of creating dictionary

def dictionary():
    dict1 = {}
    dict1['a'] = 1
    dict1['b'] = 2
    dict1['c'] = 3
    dict1['d'] = 4
    print(dict1)


# dictionary()


def dictionary_1(**kwargs):
    d = {}
    for key, value in kwargs.items():
        d[key] = value
    print(d)


# dictionary_1(a=1 ,b=2, c=3 ,d=4)


def dictionary_2():
    list1 = ['a', 'b', 'c', 'd']
    list2 = [1, 2, 3, 4]
    print(dict(zip(list1, list2)))

    tup1 = ('a', 'b', 'c', 'd')
    tup2 = (1, 2, 3, 4)
    print(dict(zip(tup1, tup2)))


# dictionary_2()

def dict_func():
    # iterate dictionary
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for i in dict1.keys():
        print(i, ":", dict1[i], " ", end=' ')
    print('\n')

    for i, j in dict1.items():
        print(i, ":", j, " ", end=' ')
    print('\n')


# dict_func()


def dict_func_1():
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print("Given dictionary:", dict1)
    print("Keys of dict1:", dict1.keys())
    print("Values of dict1:", dict1.values())
    dict2 = dict1.copy()
    print("Original dictionary dict1:", dict1)
    print("Copy of dict1 created as dict2:", dict2)
    print("Clear dictionary dict2:", dict2.clear())
    dict2 = {'f': 6, 'g': 7}
    dict1.update(dict2)
    print("After updating dict1 with dict2:", dict1)

    dict1.pop('b')  # delete given key value, here 'b'
    print("After performing pop on key 'b':", dict1)
    dict1.popitem()  # delete last key
    print("After performing popitem:", dict1)

    del dict1['f']  # delete a key by del keyword
    print("after deleting a key 'f':", dict1)

# dict_func_1()
