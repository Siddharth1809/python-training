class Employee:
    def __init__(self, name, age, eid, sal):
        self.name = name
        self.age = age
        self.eid = eid
        self.sal = sal

    def info(self):
        cname = 'Softsol'
        print('Company name:', cname)
        print('Employee name:', self.name)
        print('Employee age:', self.age)
        print('Employee id:', self.eid)
        print('Employee salary:', self.sal)


e1 = Employee('abc', 21, 101, 10000)
e1.info()
