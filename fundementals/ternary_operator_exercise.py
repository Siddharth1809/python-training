# syntax for ternary operator
# [on_True] if (expression) else [on_False]

# simple method to use ternary operator
def ternary():
    a = 10
    b = 20
    c = True if a < b else False
    print(c)


# direct method by using tuples,dict,lambda
def ternary_operator():
    a = 10
    b = 20
    tup_1 = ((a, b)[a < b])
    dict_1 = ({True: a, False: b}[a < b])
    print(tup_1)
    print(dict_1)
    lambda_1 = ((lambda: b, lambda: a)[a < b]())
    print(lambda_1)


def ternary_nested_if():
    a, b = 10, 20
    c = ('a and b both are equal' if a == b else 'a is greater than b' if a > b else 'b is greater than a')
    print(c)



