import logging


# we haven't specify the logger we are working with root logger
# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')


file_handler = logging.FileHandler('employee.log')
logger.addHandler(file_handler)

file_handler.setFormatter(formatter)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info("Created Employee: {} {}".format(self.fullname, self.email))
        # logging.info("Created Employee: {} {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp1 = Employee('John', 'Smith')
emp2 = Employee('Jane', 'Dane')
emp3 = Employee('Corey', 'Schafer')
