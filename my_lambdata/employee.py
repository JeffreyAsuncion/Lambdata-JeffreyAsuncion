# my_lambdata/employee.py

class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * 1.04) 

emp_1 = Employee("Jeffrey", "Asuncion", 50000)
emp_2 = Employee("Corey", "Schafer", 80000)

print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)