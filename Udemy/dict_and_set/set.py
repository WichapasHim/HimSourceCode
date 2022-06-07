"""farm_animal={'sheep','cow','hen'}
print(farm_animal)

for animal in farm_animal:
    print(animal)

print('*'*100)

wild_animal=set(['lion','tiger','panther','elephant','hare'])
print(wild_animal)


for animal in wild_animal:
    print(animal)

farm_animal.add('horse')
wild_animal.add('horse')

print(farm_animal)
print(wild_animal)"""


"""empty_set=set()
empty_set_2={}
empty_set.add('a')
#empty_set_2.add('a')


even=set(range(0,40,2))
print(even)
squares_tuple=(4,6,9,16,25)
sqaures=set(squares_tuple)
print(sqaures)"""


"""even=set(range(0,40,2))
print(even)
print(len(even))

sqaures_tuple=(4,6,9,16,25)
squares=set(sqaures_tuple)
print(squares)
print(len(squares))


print(even.union(squares))
print(len(even.union(squares)))

print('-'*40)

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)"""

"""even=set(range(0,40,2))
print(sorted(even))
sqaures_tuple=(4,6,9,16,25)
sqaures=set(sqaures_tuple)"""
"""print(sorted(sqaures))
print('even minus sqaure')
print(sorted(even.difference(sqaures)))
print(sorted(even-sqaures))

print('sqaures minus even')
print(sorted(sqaures.difference(even)))
print(sorted(sqaures-even))"""
















"""print('='*40)
print(sorted(even))
print(sqaures)
even.difference_update(sqaures)
print(sorted(even))"""


"""
print('symmetric even minus squares')
print(sorted(even.symmetric_difference(sqaures)))

print('sysmmetrice sqares minus even')
print(sorted(sqaures.symmetric_difference(even)))"""


"""sqaures.discard(4)
sqaures.remove(16)
sqaures.discard(8) # no error , does nothing 
print(sqaures)
try:
    sqaures.remove(8)
except KeyError:
    print('8 is not there')"""


"""even=set(range(0,40,2))
print(even)
sqaures_tuple=(4,6,16)
sqaures=set(sqaures_tuple)


if sqaures.issubset(even):
    print('sqaure is a subset f even')

if even.issuperset(sqaures):
    print('even is a superset of sqaure')
"""


even=frozenset(range(0,100,2))
print(even)
even.add(3)