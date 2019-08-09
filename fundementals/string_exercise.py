def type_string():
    a = str(input('Enter a string:'))
    print("Type of", a, 'is:', type(a))


def string_con():
    """Concatenating two strings"""
    a = str(input('Enter string1:'))
    b = str(input('Enter string2:'))
    print("Concatenation of", a, "and", b, "is:", a + " " + b)


def list_to_string():
    a = ['this', 'is', 'python']
    b = ' '.join(a)
    print('Actual list is:', a)
    print('After performing join operation:', b)
    print(type(b))


def string_to_list():
    a = 'This is python'
    b = a.split(" ")
    print('Actual string is:', a)
    print('After performing split operation:', b)
    print(type(b))


def string_format():
    name = str(input("Enter your name:"))
    age = int(input("Enter your age:"))
    bal = float(input("Enter your balance"))
    print("My self %s, my age is %d and my current account balance is %.2f $" % (name, age, bal))
    num = int(input("Enter an integer:"))
    print("Hexadecimal representation of an integer is %x" % (num))
    '''For list and dictinoary its True'''
    list1 = [1, 2, 3, 4, 5]
    print("Given list is: %s" % (list1))
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    print("Given dictionary is: %s" % (dict1))


def string_format_1():
    name = str(input("Enter your name:"))
    age = int(input("Enter your age:"))
    bal = float(input("Enter your balance"))
    print("My self {}, my age is {} and my current bank balance is {}".format(name, age, bal))
    print("My self {}, my age is {} and my current bank balance is {}".format('abc', 21, 59.452))


def string_operations():
    a = str(input("Enter a string:"))
    print("String is:", a)
    print("occurrence of 'p' in string:", a.count('p'))
    print("String in upper case:", a.upper())
    print("String in lower case:", a.lower())
    print("Capitalise first letter in string:", a.capitalize())
    b = a.split(" ")
    '''split operation returns a list '''
    print("Splitting at space:", b)
    print("Join a string by - :", '-'.join(b))
    print("Reverse a string:", a[::-1])
