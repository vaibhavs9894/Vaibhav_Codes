a = {1,2,3,4,5,6,7,8,9,10}
b = {1,2,3,4}
c = {6,7,8,9,10}
d = {3,4,5,6,7,8}
e = {11,22,33}

# set functions
# add
# remove
# clear
# update
# pop

# issubset
# issuperset
# isdisjoint - check is two sets are unrelated or not
# union
# intersection
# difference
# symmetric_difference

e.add('apple')
c.remove(9)
d.update([1,2,56,6,77,8,78]) # add a seq  to an existing set
e.pop() # pop out a random value from a set

print(a)
print(b)
print(c)
print(d)
print(e)

print(a.issuperset(c),'a is superset of c')
print(a.issuperset(d),'a is superset of d')

if b.issubset(a):
    print("b is subset of a")
else:
    print('b is not subset of a')
if e.issubset(d):
    print("e is subset of d")
else:
    print('e is not a subset of d')

if a.isdisjoint(e):
    print('a and e me koi rishta  nhi')
else:
    print('a and e are connected')

if b.isdisjoint(d):
    print('b and d me koi rishta  nhi')
else:
    print('b and d are connected')

# set math

# union, take every unique values from the set
print('union')
print(a.union(d))
print(a|d)  # | is operator for union

# difference, take unique value fromt he first set only
print('difference')
print(a.difference(d))
print(a-d) # - is difference operator

# intersection, take the common values from each set
print('intersection')
print(a.intersection(d))
print(a & d)

# symmetric differece, remove common values from each set
print('symmetric differece')
print(a.symmetric_difference(d))
print(a ^ d)