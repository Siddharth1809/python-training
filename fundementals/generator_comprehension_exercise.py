nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for i in nums:
        yield i * i


result = gen_func(nums)
# one approach
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# another approach
for num in result:
    print(num)

# using generator comprehension
def gen_comprehension():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = (n * n for n in nums)

    # print(list(result))
    for k in result:
        print(k)


gen_comprehension()
