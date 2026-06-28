# greeting = "Hello"

# name = 'Micheal'

# message = greeting + ' ' + name +  '. Welcome!'

# message = f'{greeting.upper()} , {name.upper()}.Welcome!'

# print(help(str.lower))

# num = 3.555

# #um_2 = '200'

# num_1 = int(num_1)
# num_2 = int(num_2)

# print(num_1 / num_2)

# courses = ['History', 'Math', 'Physics', 'CompSci']
# for  index,course in enumerate(courses, start =1):
#     print(index,course)


# Mutable:LIST
# list_1  = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'
# print(list_1)
# print(list_2)

# Non-Mutable:TUPLE
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.union(art_courses))


# language = 'Python'
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'C+':
#     print('Language is C+')
# else:
#     print('No match')

# not
# user = 'Administrator'
# logged_in = False

# if not logged_in:
#     print('Please log in first')
# else:
#     print('Welcome Administrator')

# a = [1, 2, 3]
# b = a

# print(id(a))
# print(id(b))
# print (id(a) == id(b))

# nums = [1, 2, 3, 4, 5, 6, 7]

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# NESTED LOOP
# for i in range(1, 11):
#     print(i)

# WHILE LOOP
# x = 0
# while True:
#     # if x == 5:
#     #    break
#     print(x)
#     x += 1

# def hello_func(greeting , name = 'You'):
#     return '{}, {}' .format(greeting , name)

# # print(hello_func('Hi' , name = 'Corey'))

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# courses = ['Math' , 'Art']
# info = {'name' : 'John' , 'age' : 22 }
# student_info(*courses , **info)

# # Number of days per month . First value placeholder for indexing purposes.
# month_days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

# def is_leap(year):
#     """Return True for leap years, false for non-leap years."""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year , month):
#     """Return number of days i  that month in that years."""
#     # year 2017
#     # month 2
#     if not 1 <= month <= 12:
#         return 'Invalid Month '

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]

# print (days_in_month(2017, 2))


import os
from datetime import datetime
os.chdir(r'C:\Users\Asus\PycharmProjects')
print(os.environ.get('USERPROFILE'))
print(os.environ.get('USERPROFILE'))
file_path = os.path.join(os.environ.get('USERPROFILE'),'test.txt')
print(file_path)

print(dir(os.path))
print(os.path.dirname(r'\tmp\test.txt'))
print(os.path.split(r'\tmp\test.txt'))
print(os.path.exists(r'\tmp\test.txt'))


# FILE OBJECTS
with open('manii.jpg', 'rb') as rf:
    with open('manii_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len( rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

import os
print(os.getcwd())
os.makedirs('patrons.csv')













