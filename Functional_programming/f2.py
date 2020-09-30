import collections
from pprint import pprint
Scientists = collections.namedtuple('Scientists', [
    'name',
    'age',
])
scientists = [Scientists(name='kaushik', age=21),
              Scientists(name='kau', age=20)]
print(scientists)
# It will print in one line
pprint(scientists)
# when we use pprint it will print line by line
# We cannot modify anything here bcz we are using an immutable ds called named tuple
# but we can delete an instance(object) like:
del scientists[0]
print(scientists)
# [Scientists(name='kau', age=20)]
# This happened bcz we used an mutable data structure wrapping the immutable data structure!
# So, the best way to handle this is instead of list we can use a tuple.
scientists2 = (Scientists(name='kaushik', age=21),
               Scientists(name='kau', age=20))
print(scientists2)
# (Scientists(name='kaushik', age=21), Scientists(name='kau', age=20))
pprint(scientists2)
# So now its not possible to delete an instajnce by del as tuple is immutable
# So try using the immutable data structures if you are trying to work with functional programming style!