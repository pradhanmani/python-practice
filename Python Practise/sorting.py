######## SORTING
# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# s_li = sorted(li, reverse = True)

# print('Sorted Variable:\t', s_li)

# li.sort(reverse = True)

# print('Original Variable:\t', li)



##### Tuple
# tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# s_tup = sorted(tup)
# print('Sorted Tuple:\t' , s_tup)
# print('Original Tuple:\t', tup)

######## Dictionary

# di = {'name': 'Corey ', 'job': 'programming', 'age': 'None', 'os': 'Windows'}
# s_di = sorted(di)
# print('Sorted Dict:\t', s_di)
# print('Origianl  Dict:\t',di)

#######LIST IN NEGATIVE VALUE

# li  = [-6, -5, -4 ,1, 2, 3 ]
# s_li = sorted(li, key=abs)  #abso;ute value which brings the value in the order
# print('SORTED LIST:\t' , s_li)
# print('ORIGINAL LIST:\t' , li)

#########

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '({}, {}, ${})' .format(self.name, self.age, self.salary)
    
from operator import attrgetter
    
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43,90000)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.salary

s_employees = sorted(employees, key=attrgetter('name'))

print(s_employees)

