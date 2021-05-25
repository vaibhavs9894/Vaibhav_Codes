x = (1,2,3,4)
y = 12,34,56,78

print(x)
print(y)
print(type(x))
print(type(y))

a = [1,23,4,5,65]
at = tuple(a) # list to tuple conversion
print('list =>',a, 'tuple =>', at)

name = 'Kaladin'
namet = tuple(name)
print('string =>',name, 'tuple =>', namet)

a = 1
b = 2
c = 3
d = a,b,c
print(d)

# error => d[3] = 10

# function
# count
# index
a = (1,2,3,3,3,3,23,1,1,1,1,1,2,2,2,3)
print("counting all 3s =" ,a.count(3))
print("index of 23 = ", a.index(23))