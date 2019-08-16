def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))  # this additional
        # functionality can be added without modifying the original one
        return original_function()

    return wrapper_function


def display():
    print("Display function ran")


decorator_display = decorator_function(display)
print(decorator_display.__name__ ) # wrapper function
decorator_display()  # call like any other function

print('*' * 50)


# @ decorator property
# bu using this @ property we can directly call the function
def decorator_function(original_function):
    # with out this *args and **kwargs we can't call display_info function or else it gives error
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(
            original_function.__name__))  # this additional functionality can be added without modifying the original
        # one
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function  # it is similar to decorator_display = decorator_function(display)
def display():
    print("Display function ran")


@decorator_function
def display_info(name, age):
    print("Display info with arguments ({},{})".format(name, age))


display()
display_info('John', 25)

print('*' * 50)


# class decorator

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("Display function ran")


@decorator_class
def display_info(name, age):
    print("Display info with arguments ({},{})".format(name, age))


display()
display_info('Mack', 26)
