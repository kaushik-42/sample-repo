# MAP() Function:
# map(func,*iterables)
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
# pprint(scientists2)
# But if we want to create a new dictionary of values only considering name and new column we are creating i.e dob
scientists_m = tuple(
    map(lambda x: {'name': x.name, 'dob': 2020-x.age}, scientists2))
print(scientists_m)
pprint(scientists_m)
"""
Result:
({'dob': 2000, 'name': 'kaushik'},
 {'dob': 2000, 'name': 'chow'},
 {'dob': 2001, 'name': 'Tk rahul'},
 {'dob': 2000, 'name': 'Rohith'})
So without making use of the loops statements we created and mapped the scientists tuple to this in one go.
"""
# The map() Function vs Generator Expressions:
# we can also do the above thing in a more pythonic way using list comprehension:
print([{'name': x.name, 'dob': 2020-x.age} for x in scientists2])
"""
[{'name': 'kaushik', 'dob': 2000}, {'name': 'chow', 'dob': 2000}, {'name': 'Tk rahul', 'dob': 2001}, {'name': 'Rohith', 'dob': 2000}]
"""
# To cast it into non immutable data type:
m = tuple({'name': x.name, 'dob': 2020-x.age} for x in scientists2)
# {'name': x.name, 'dob': 2020-x.age} for x in scientists2 is called the gererator expression.
# A genarator object is something that we iterate upon.
pprint(m)
"""
({'dob': 2000, 'name': 'kaushik'},
 {'dob': 2000, 'name': 'chow'},
 {'dob': 2001, 'name': 'Tk rahul'},
 {'dob': 2000, 'name': 'Rohith'})
"""
# What is the use of this?
# We can transform the input data in all kinds that we need and there are no side affects and it can be reusable.
# ex: we can convert the input data i.e names to capital letters
pprint(tuple({'name': x.name.upper(), 'dob': 2020-x.age} for x in scientists2))
"""
({'dob': 2000, 'name': 'KAUSHIK'},
 {'dob': 2000, 'name': 'CHOW'},
 {'dob': 2001, 'name': 'TK RAHUL'},
 {'dob': 2000, 'name': 'ROHITH'})
"""