# difference between a normal def defined and lambda function
# def defined function
def cube(x):
    return x * x * x


print(cube(7))

# lambda function
new = lambda x: x * x * x

print(new(7))

# lambda with filter
# get odd elements from list1
list1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
result = list(filter(lambda n: n % 2 != 0, list1))
print(result)

# lambda with map
# get double of list
list2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
result_1 = list(map(lambda n: n * 2, list2))
print(result_1)

# lambda with reduce
from functools import reduce

list3 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
sum = reduce(lambda x, y: x + y, list3)
print(sum)

# iterating over dictionary using map and lambda
dict1 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print("My dict:", dict1)
key = list(map(lambda x: x['name'], dict1))
print("Keys from dict1:", key)
value = list(map(lambda x: x['points'], dict1))
print("Values from dict1:", value)

# filter dictionary by key values
dict1 = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print("My dict:", dict1)
temp_python = list(filter(lambda x: x['name'] == 'python', dict1))
print("For python as a key:", temp_python)
temp_java = list(filter(lambda x: x['name'] == 'java', dict1))
print("For java as a key:", temp_java)

# reduce example for sum from 1 to 101
count = 0
for i in range(1, 101):
    count += i
print(count)

total = reduce(lambda x, y: x + y, range(1, 101))
print(total)

# given a list of string find all palindromes
# by normal approach
list_str = ["geeks", "geeg", "keek", "practice", "aa"]
final = []
for i in list_str:
    if i == i[::-1]:
        final.append(i)
print(final)

# by lambda and filter approach
final_result = list(filter(lambda x: x == x[::-1], list_str))
print(final_result)
