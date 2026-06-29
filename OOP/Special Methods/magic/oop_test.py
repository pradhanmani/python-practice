
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):       ####Dunder Init  (Initialize the object)
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):          ###Dunder repr (Unambiguous representation of an object.Representation for developers)
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):           ###Dunder Str (Show the object as text)
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):        ####Dunder Add (For Summation)
        return self.pay + other.pay

    def __len__(self):               ####Dunder Len  (For Length)
        return len(self.fullname())


emp_1 = Employee('Mani', 'Pradhan', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(emp_1 + emp_2)

print(len(emp_1))

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

