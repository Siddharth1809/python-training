from functools import partial


def multiply(x, y):
    return x * y


new = partial(multiply, 4)
print(new(3))


def normal(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


part_func = partial(normal, 3, 1, 4)
print(part_func(5))


def add(a, b, c):
    return 100 * a + 10 * b + c


add_part = partial(add, c=2, b=1)
print(add_part(3))
