x = {1,2,3,4,5}
y = {'apple','banana','mango'}
z = {1,2,3,3,3,3,1,'apple',11,2,2,2,21,1,1,2}

print(x)
print(y)
print(z) # duplicate are removed
print(type(z))

a = [1,2,3,4,5] # list
b = (2,3,3,31)  # tuple

# list - set - tuple are interconvertible
a_set = set(a)
b_set = set(b)
print(a,a_set)
print(b,b_set)

# set values cannot be indexed or sliced

for i in a_set:
    print(i,end='')

# error print(set([y,z]))