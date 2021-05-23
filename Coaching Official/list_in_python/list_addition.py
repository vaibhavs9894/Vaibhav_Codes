# add each item from 2 list and store result in 3rd list

x = [31,22,33,13,42,53,56,61,27]
y = [23,322,13,23,43,52,6,7]

z = []
for i,j in zip(x,y):
    z.append(i + j)

print(x)
print(y)
print(z)

print(x+y) # just concatenates both list together, so not to be used