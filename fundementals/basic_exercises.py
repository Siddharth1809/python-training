def type_check(a, b, c):
    """Enter different values in a,b and c and check types of it"""
    print(type(a))
    print(type(b))
    print(type(c))


def type_complex(a, b):
    """enter a and b as real and imaginary value respectively"""
    result = complex(a, b)
    print("complex number is:", result)


def type_int(a):
    """type casting of a in int"""
    result = int(a)
    print(result)


def type_float(a):
    """type casting of a in float"""
    result = float(a)
    print(result)


def show_types():
    mystr = str(input("Enter a string:"))
    myint = int(input("Enter an int number:"))
    myfloat = float(input("Enter a float number"))
    print("String: %s" % (mystr))
    print("Integer: %s" % (myint))
    print("Float: %f" % (myfloat))
    print("Float: %.2f" % (myfloat))
    print("Float: %f" % (round(myfloat, 3)))


def operators():
    """Basic arithmetic operators"""
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    print("Addition:", a + b)
    print("Substraction:", a - b)
    print("Multiplication:", a * b)
    print("divison:", round(a / b, 2))
    print("Reminder:", a % b)
    print("square of", a, "is:", a ** 2)
    print("cube of", a, "is:", a ** 3)
    print("square root of", a, "is", a ** 0.5)


def boolean_operators():
    a = 2
    b = 2
    print("Value of a:", a)
    print("Value of b:", b)
    print("identity operator for a is b:", a is b)
    a = 2
    b = 3
    print("Value of a:", a)
    print("Value of b:", b)
    print("identity operator a is not b:", a is not b)
    a = True
    print("Value of a:", a)
    print("Not a operation:", not a)

    list1 = [1, 2, 3, 4]
    print("list is:", list1)
    print("Membership operator for 1 in list1:", 1 in list1)
    print("Membership operator for 5 in list1:", 5 in list1)
    print("Membership operator for 5 not in list1:", 5 not in list1)

    x = ['a', 'b', 'c']
    y = ['a', 'b', 'c']
    print("Value of x:", x)
    print("Value of y:", y)
    print(" == operator for x==y:", x == y)
    print(" != operator for x!=y:", x != y)
