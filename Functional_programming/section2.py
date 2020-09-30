# Filter Function is one of the functional programing primitives in python programs.
# Lets use the scientists dataset and let's play with filtering!
"""
filter() is one of the functional programming primitives (or building blocks) 
available in Python and that it’s useful in a number of contexts.
filter() takes another function object, and you can define a function object 
inline with lambda expressions.
"""
import collections
from pprint import pprint
Scientists = collections.namedtuple('Scientists', [
    'name',
    'age',
    'comp'
])

scientists2 = (Scientists(name='kaushik', age=20, comp='Microsoft'),
               Scientists(name='chow', age=20, comp='Adobe'),
               Scientists(name='Tk rahul', age=19, comp='Google'),
               Scientists(name='Rohith', age=20, comp='Oracle'))
# print(scientists2)
#m = scientists2(lambda x: x.age == 20)
# print(m)
"""
Traceback (most recent call last):
  File "section2.py", line 16, in <module>
    m = scientists2(lambda x: x.age == 20)
TypeError: 'tuple' object is not callable
"""
fs = filter(lambda x: x.comp == 'Microsoft', scientists2)
# print(fs)
# <filter object at 0x10ed51940>
# So it is returning a iterator object where you have to unpack it by using next keyword
# print(next(fs))
# print(next(fs))
"""
Scientists(name='kaushik', age=21, comp='Microsoft')
Scientists(name='kau', age=20, comp='Microsoft')
"""
# print(next(fs)) If we do this we get:
"""
Traceback (most recent call last):
  File "section2.py", line 30, in <module>
    print(next(fs))
StopIteration
BCZ WE HAVE NO MORE TO UNPACK FROM THE FILTER FUNCTION
"""
# With the results that we got we can convert this into some immutable data structure!
fs = tuple(filter(lambda x: x.comp == 'Microsoft', scientists2))
pprint(fs)
fs1 = tuple(filter(lambda x: x.comp == 'Google' or x.age == 20, scientists2))
pprint(fs1)
"""
(Scientists(name='kaushik', age=20, comp='Microsoft'),
 Scientists(name='chow', age=20, comp='Adobe'),
 Scientists(name='Tk rahul', age=19, comp='Google'),
 Scientists(name='Rohith', age=20, comp='Oracle'))
"""
# Instead of lambda function we can also create a function like:


def age_filter_comp(x):
    return x.comp == 'Google' and x.age == 20


fs1 = tuple(filter(age_filter_comp, scientists2))
pprint(fs1)
# The above step also works exactly the same as the lambda functions.
# But why should we write code like this and not a for loop:
# Bcz we can apply the transformations in a simplified way and
# a cleaner way where its flexible enough to change the properties but
# I dont mean that this way of writing code is good but this relies on application
# or evaluating functions rather than writing stuff and also this can make things a lot
# easier if we deal with parallel programming.
# Python also has a wonderful thing called as list comprehensions(can be a replacement to filter):
pprint([x for x in scientists2 if (x.age == 20 or x.comp == 'Google')])
"""
[Scientists(name='kaushik', age=20, comp='Microsoft'),
 Scientists(name='chow', age=20, comp='Adobe'),
 Scientists(name='Tk rahul', age=19, comp='Google'),
 Scientists(name='Rohith', age=20, comp='Oracle')]
"""
# And also tuple(list()) is a tuple ex: tuple([1,2,3]) is (1,2,3)
