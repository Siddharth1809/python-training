import pickle


class Employee:

    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.eaddr)


file = open("new_emp_data.txt", "ab")
n = int(input("Enter number of employees:"))
for i in range(n):
    eno = int(input("Enter emp no:"))
    ename = input("Enter emp name:")
    esal = int(input("Enter emp salary:"))
    eaddr = input("Enter emp address:")

    emp_obj = Employee(eno, ename, esal, eaddr)
    pickle.dump(emp_obj, file)

file.close()

file = open("new_emp_data.txt", "rb")
print("Employee Details")

while True:
    try:
        obj = pickle.load(file)
        obj.display()
        print()
    except EOFError:
        print("All Employees completed")
        break
file.close()
