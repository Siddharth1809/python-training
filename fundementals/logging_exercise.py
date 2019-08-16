import logging

# logging.basicConfig(filename='sample.log', format='%(asctime)s:%(levelname)s:%(message)s:', level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')


file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(level=logging.DEBUG)  # run in console

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


num1 = 10
num2 = 5

add_result = addition(num1, num2)
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))
# logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = subtraction(num1, num2)
logger.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))
# logging.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))

mul_result = multiplication(num1, num2)
logger.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))
# logging.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))

div_result = division(num1, num2)
logger.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
# logging.debug('Div: {} / {} = {}'.format(num1, num2, div_result))
