num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Given num_list is:", num_list)


# suppose I want num_list in result_list then by using standard method
def list_append(num_list):
    result_list = []
    for i in num_list:
        result_list.append(i)
    return "save num_list into result_list:", result_list


print(list_append(num_list))


# change list_append method by using list comprehension
def list_comprehension_append(num_list):
    result_list = [i for i in num_list]
    return "save num_list into result_list by list comprehension:", result_list


print(list_comprehension_append(num_list))


# suppose I want square of num_list then by using standard method
def list_square(num_list):
    result_list = []
    for i in num_list:
        result_list.append(i * i)
    return "square of num_list elements into result_list:", result_list


print(list_square(num_list))


# change list_square method by using list comprehension
def list_comprehension_square(num_list):
    result_list = [i * i for i in num_list]
    return "square of num_list elements into result_list by list comprehension:", result_list


print(list_comprehension_square(num_list))


# works same as list comprehension
def using_map_lambda():
    # result_list = map(lambda n: n * n, num_list)
    # return result_list      #this creates an map object
    # return "square of n in num_list:",list(result_list)

    result_list1 = list(map(lambda n: n * n, num_list))
    return "square of n in num_list:", result_list1


print(using_map_lambda())


# I want even elements from num_list
def list_comprehension_even(num_list):
    result_list = [n for n in num_list if n % 2 == 0]
    return "Even elements from num_list:", result_list


print(list_comprehension_even(num_list))


# works same as list comprehension
def using_filter_lambda():
    result_list = list(filter(lambda n: n % 2 == 0, num_list))
    return "Even elements from num_list:", result_list


print(using_filter_lambda())


# I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
def list_pair():
    result_list = []
    for i in 'abcd':
        for j in range(4):
            result_list.append((i, j))
    return "(letter,num) pair:", result_list


print(list_pair())


def list_comprehension_pair():
    result_list = [(letter, num) for letter in 'abcd' for num in range(4)]
    return "(letter,num) pair using list comprehension:", result_list


print(list_comprehension_pair())


# list comprehension for values divisible by 2 and 5
def list_comprehension_div():
    result_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
    return "In range of 100 elements divisble by 2 and 5 are:", result_list


print(list_comprehension_div())


# check even and odd if else in list comprehension
# in below function 'odd' if i % 2 != 0 else 'even' is a ternary operator
def list_even_odd():
    result_list = ['odd' if i % 2 != 0 else 'even' for i in range(10)]
    return 'Even and Odd in range of 10 elements:', result_list


print(list_even_odd())
