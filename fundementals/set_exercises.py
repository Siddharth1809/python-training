# both creates same set
set1 = set([1, 2, 3, 4, 5, 6, 7, ])
print(set1)

set2 = {1, 2, 3, 4, 5, 6, 7}
print(set2)

# to create an empty set
set1 = {}  # this creates an empty dictionary
set2 = set()
print(type(set1))
print(type(set2))


# set removes duplicate values
def set_unique():
    set_val = {1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9}
    print(set_val)


# adding an element to set
def self_add():
    my_set = {1, 2, 3, 4, 5}
    print("Actual set:", my_set)
    my_set.add(6)  # just take one argument
    print("After add operation:", my_set)


# to add multiple elements
def self_update():
    my_set = {1, 2, 3, 4, 5}
    temp = {6, 7, 8}
    print("Actual set:", my_set)
    my_set.update(temp, {7, 8, 9})
    print("After add operation:", my_set)


# to remove an element
def self_remove():
    my_set = {1, 2, 3, 4, 5}
    print("Actual set:", my_set)
    my_set.remove(5)
    print("After remove an element:", my_set)


# the difference between remove and discard is that if we remove an element
# which doesn't exists in set then it throws a key error
# but using discard it doesn't give error


# discard method
def self_discard():
    my_set = {1, 2, 3, 4, 5}
    print("Actual set:", my_set)
    my_set.discard(6)
    print("After discard an element 5:", my_set)


# intersection operation
def self_intersection():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    set3 = {3, 4, 5}
    set4 = set1.intersection(set2, set3)
    print("Intersection of all sets:", set4)


# difference operation
def self_difference():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    set3 = {3, 4, 5}
    diff_set1 = set1.difference(set2, set3)  # we running difference method on set1 so it gives {1}
    diff_set2 = set2.difference(set1, set2)
    diff_set3 = set3.difference(set1, set2)
    print("Difference on set1:", diff_set1)
    print("Difference on set2:", diff_set2)
    print("Difference on set3:", diff_set3)


# symmetric difference and it takes only one argument
def self_symmetric_difference():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    set3 = {3, 4, 5}
    sym_set1 = set1.symmetric_difference(set2)
    sym_set2 = set2.symmetric_difference(set3)
    sym_set3 = set3.symmetric_difference(set1)
    print("Symmetric Difference on set1 and set2:", sym_set1)
    print("Symmetric Difference on set2 and set3:", sym_set2)
    print("Symmetric Difference on set3 and set1:", sym_set3)


# remove duplicate from a list
def get_list_unique():
    list1 = [1, 2, 3, 1, 2, 3]
    list2 = list(set(list1))
    print("List contains duplicate values:", list1)
    print("List after removing duplicates values:", list2)


# intersection and difference methods in set
def set_operations():
    employees = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    gym_members = ['d', 'g', 'a']
    developers = ['e', 'a', 'c', 'h', 'd']
    result_intersect = set(gym_members).intersection(set(developers))
    print("Employees which are gym members and developers:", result_intersect)

    result_diff = set(employees).difference(set(gym_members), set(developers))
    print("Employees which are neither gym members nor developers:", result_diff)


# count number of vowels present in string using set
def find_vowel():
    my_str = str(input("Enter a string:"))
    set1 = set('aeiouAEIOU')
    count = 0
    for i in my_str:
        if i in set1:
            count += 1
    print(count)