import collections
scientists = [{'name': 'kaushik', 'age': 20},
              {'name': 'kaushik2', 'age': 21}]
print(scientists)
# But a list is a mutable data structure and we can edit that so this is not clean code
# ex:
scientists[0]['name'] = 'kau'
print(scientists)
# if we have a typo while creating an another item then there is no validation and it would add that to the list!
# so then we define the collections package and in that we require namedtuple
Scientists = collections.namedtuple('Scientists', [
    'name',
    'age',
])
print(Scientists)
# <class '__main__.Scientists'>
Scientists(name="kau", age=20)
kau2 = Scientists(name="kau1", age=21)
print(kau2.name)
print(kau2.age)
# kau1
# 21
kau2.name = "kauhik"
print(kau2.name)
"""
Traceback (most recent call last):
  File "f1.py", line 23, in <module>
    kau2.name = "kauhik"
AttributeError: can't set attribute
""" # bcz we used a immutable data structure it means that we cant modify that so its safe!
