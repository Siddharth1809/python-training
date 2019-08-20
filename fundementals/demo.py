
def decorator_function(original_function):
    # with out this *args and **kwargs we can't call display_info function or else it gives error
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)  # to call display function's print statement
        print("wrapper executed this before {}".format(
            original_function.__name__))  # this additional functionality can be added without modifying the original
        # one

        return result

    return wrapper_function


@decorator_function  # it is similar to decorator_display = decorator_function(display)
def display():
    print("Display function ran")


display()


