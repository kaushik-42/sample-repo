# Reduce Function(): we have to import reduce from functools
from functools import reduce
"""reduce():The following is the doc string of reduce
param function: Callable[[_T, _S], _T]

reduce(function, sequence[, initial]) -> value
Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
"""
# reduce(function,sequence[,initial])- what it does is it applies the function repeatedly on the sequence untill we land up with a number
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
names_and_ages = tuple({'name': x.name, 'DOB': 2020-x.age}
                       for x in scientists2)
# pprint(names_and_ages)
total_age = reduce(
    lambda acc, val: acc+val['DOB'], names_and_ages, 0
)
# 0 is the initial value and we are adding up all the values
print(total_age)
# 8001
# Alternative to calculate this is:
m = (sum(x['DOB'] for x in names_and_ages))
print(m)
# 8001
# why do I need to use reduce()?


def reducer(acc, val):
    acc[val.comp].append(val.name)
    return acc


Scientists_by_comp = reduce(
    reducer, scientists2, {'Microsoft': [],
                           'Oracle': [], 'Google': [], 'Adobe': []}
)
print(Scientists_by_comp)
"""
{'Microsoft': ['kaushik'], 'Oracle': ['Rohith'], 'Google': ['Tk rahul'], 'Adobe': ['chow']}
"""
# Better way to do it:

Scientists_by_comp = reduce(
    reducer, scientists2, collections.defaultdict(list)
)
print(Scientists_by_comp)
"""
defaultdict(<class 'list'>, {'Microsoft': ['kaushik'], 'Adobe': ['chow'], 'Google': ['Tk rahul'], 'Oracle': ['Rohith']})
"""
