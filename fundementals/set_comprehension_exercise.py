# get unique values from a list
def set_add():
    nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
    result = set()
    for i in nums:
        result.add(i)
    print("Result set is:", result)


set_add()


# get uniques values from a list using set comprehension
def set_comprehension():
    nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
    result_set = {n for n in nums}
    print("Get unique result set using set comprehension:", result_set)


set_comprehension()
