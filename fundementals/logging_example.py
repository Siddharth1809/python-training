import logging
from fundementals import logging_exercise_1

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('sample_1.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result


num1 = 10
num2 = 0

add_result = add(num1, num2)
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))
# logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logger.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))
# logging.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))

mul_result = multiply(num1, num2)
logger.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))
# logging.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))

div_result = divide(num1, num2)
logger.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
# logging.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
