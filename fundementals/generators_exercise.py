# this is the one way to print square of list numbers using empty list
def square_number(num):
    result = []
    for i in num:
        result.append(i * i)
    return result


num = [1, 2, 3, 4, 5]
my_nums = square_number(num)
print(my_nums)


# square numbers in a given list using generator
def square_using_generator(nums):
    for i in nums:
        yield i * i


nums = [1, 2, 3, 4, 5]
my_nums_1 = square_using_generator(nums)
print(my_nums_1)  # this creates an generator object

# iterate one by one
print(next(my_nums_1))
print(next(my_nums_1))
print(next(my_nums_1))
print(next(my_nums_1))
print(next(my_nums_1))


# print(next(my_nums_1))  # this gives exception as stop iteration


# another approach of generator
def square_generator(my_list):
    for i in my_list:
        yield i * i


my_list = [1, 2, 3, 4, 5]
result_list = square_generator(my_list)

for item in result_list:
    print(item)

# a basic example of list comprehension
result = [x * x for x in [1, 2, 3, 4, 5]]
print(result)

# if use () instead of [] in result then it creates a generator object
result = (x * x for x in [1, 2, 3, 4, 5])
print(result)  # creates generator object
print(list(result))  # to convert in list


# this function prints top ten values
def top_ten():
    a = 1
    while a <= 10:
        yield a
        a += 1


value = top_ten()
for j in value:
    print(j)

print('*' * 10)


# this function prints top ten square values
def top_ten_squares():
    n = 1
    while n <= 10:
        yield n * n
        n += 1


val = top_ten_squares()
for k in val:
    print(k)


# fibonacci series for given input number of terms
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib_result = fibonacci(5)
for k in fib_result:
    print(k)
