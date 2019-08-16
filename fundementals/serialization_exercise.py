import pickle


class Employee:

    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.eaddr)


with open("emp.data", "wb") as file:
    emp_obj = Employee(100, 'abc', 1000, 'Hyd')
    pickle.dump(emp_obj, file)
    print("Pickling of Employee object completed")

with open("emp.data", "rb") as file:
    obj = pickle.load(file)
    print("Employee information after unpickling")
    obj.display()
