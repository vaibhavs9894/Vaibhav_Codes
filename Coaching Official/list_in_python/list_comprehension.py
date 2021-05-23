# example, with basic logic
x = [1,2,3,4,54,23,22,21]

x2 = []                     # blank list
for i in x:                 # loop 
    sqr = i**2              # sqr of each val
    x2.append(sqr)          # stored in x2

print(x)
print(x2)

# can be done with comprehension with one line
x = [1,2,3,4,5,6,7,8]

# new_list = [operation loop]
x2 = [i**2 for i in x]      # comphresion makes code smaller

print(x)
print(x2)
