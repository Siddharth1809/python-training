# some practical examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info("Ran with args:{} and kwargs:{}".format(*args, **kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {}".format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
def display_info(name, age):
    print("Display info ran with arguments ({},{})".format(name, age))


display_info('John', 25)
display_info('Mack', 26)

print('*' * 50)

import time


@my_timer
def display_info(name, age):
    time.sleep(1)
    print("Display info ran with arguments ({},{})".format(name, age))


display_info('John', 25)
display_info('Mack', 26)

print('*' * 50)


# @my_timer
@my_logger
@my_timer  # this functionality similars to display_info = my_logger(my_timer(display_info))
# @my_timer executes first

def display_info(name, age):
    print("Display info ran with arguments ({},{})".format(name, age))


display_info('John', 25)
display_info('Mack', 26)
