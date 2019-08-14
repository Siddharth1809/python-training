try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print(a / b)
    raise ZeroDivisionError
except ZeroDivisionError as e1:
    print("exception handles")

str1 = str(input("Enter a string:"))

try:
    num = int(input("Enter a number:"))
    print(str1 + num)
except Exception as e:
    print("Exception occurs", e)
except ValueError as ve:
    print("exception1 occurs", ve)


class MyError(Exception):
    def __init__(self, value):
        self.value = value


try:
    raise MyError(2)
except MyError as e:
    print("My Exception occurred,value:", e.value)


# If the expression is false, Python raises an AssertionError exception
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


Temperature = int(input("Enter value of temperature:"))
print(KelvinToFahrenheit(Temperature))

