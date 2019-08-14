def argument(a, b, c, d):
    print("First Argument is:", a)
    print("Second Argument is:", b)
    print("Third Argument is:", c)
    print("Fourth Argument is:", d)


argument(5, 2, 4, 7)

argument(c=4, b=1, d=5, a=3)

"""
to pass variable number of arguments we use *args and **kwargs
* is known as asterisk


*args: passes variable number of non keyword arguments tuple
       can perform all list operation
       single * (asterisk)
       *name can be anything
       

**kwargs: passes variable number of keyword argument dictionary
          can perform all dictionary operation
          double ** (asterisk)
          **name can be anything

"""


# *args

def sum_all(*num):
    sum = 0  # type of num is tuple but perform all operations of list
    for i in num:
        sum += i
    print("Sum is:", sum)


sum_all(10, 20)
sum_all(10, 20, 4, 8)
sum_all(4, 4, 5, 9, 3, 1, 7, 8, 2, 1)
sum_all(10)


def add_num(*num1):
    temp = [10, 20]
    print(type(num1))  # type of num1 is tuple but perform list operations
    for j in num1:
        temp.append(j)
    print(temp)


add_num([10, 20, 30, 40])


def intro(**data):
    print("Data type of argument:", type(data))  # type is dict and if print(data) it returns a dictionary containing
    # key and values
    print(data)
    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="abc", Lastname="p", empid=100, addr="Ahm")
intro(Firstname="pqr", addr="Hyd", Lastname="x", email="abc@gmail.com", cname="soft")
