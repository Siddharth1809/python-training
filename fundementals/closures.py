# nested function
def outerFunction(msg):
    text = msg

    def innerFunction():  # inner function is accessed inside the body of outerFunction
        print(text)  # uses text as a non-local variable

    return innerFunction()


outerFunction("Python")


# a basic example of first class function
def square(x):
    return x * x


def cube(x):
    return x * x * x


def my_final(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_final(square, [1, 2, 3, 4])
print(squares)

cubes = my_final(cube, [1, 2, 3, 4])
print(cubes)

# closures
def outerFunction(msg):
    text = msg

    def innerFunction():  # inner function is accessed inside the body of outerFunction
        print(text)  # uses text as a non-local variable

    return innerFunction  # return function without parenthesis


myFunction = outerFunction("Program")
print(myFunction.__name__)  # we can execute this variable just like another function
myFunction()

hi_Function = outerFunction("Hi")
hi_Function()
hello_Function = outerFunction("Hello")
hello_Function()
bye_function = outerFunction("Bye")
bye_function()


def html_tag(tag):
    def wrap_text(in_msg):
        print("<{0}> {1} </{0}>".format(tag, in_msg))

    return wrap_text


title_func = html_tag("head")
title_func("title")

body_func = html_tag("body")
body_func("This is an article")

para_func = html_tag("p")
para_func("Test paragraph")


def main_func(func):
    def sub_func(*args):
        print(func(*args))

    return sub_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_main_func = main_func(add)
add_main_func(3, 5)

sub_main_func = main_func(sub)
sub_main_func(20, 10)
