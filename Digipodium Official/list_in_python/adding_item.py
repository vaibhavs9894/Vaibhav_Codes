x = []
y = [1,2,3]

# adding single values to list
x.append(10)
x.append(20)
x.append(30)

y.append(4)
y.append(6)
y.append(8)

# insert single values to a list
z = [1,3,4,5,6,7,8,9,10]
z.insert(1,2) # insert 2 at index 1 and shift everything to right
z.insert(3,20) # insert 20 at index 3

print(x)
print(y)
print(z)

# replace a value at an index (no function, direct assignment)
x[0] = 100
x[-1] = 400
z[3] = 3

print(x)
print(y)
print(z)

# join a list to existing list
x.extend([22,33,44,55])
y.extend(x)
z.extend(y)
print(x)
print(y)
print(z)