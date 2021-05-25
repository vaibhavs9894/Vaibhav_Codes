# datatypes => python has 9 basics types. every datatype refers to a class written in python, which you dont need to understand

#  integer (int)
a = 1
b = 2302112
c = +2382
d = -2312

print(type(a),type(b),type(c),type(d))

# float
a = 1.1
b = -3.115123
c = .231223131231231231
d = 1.2e-10

print(type(a),type(b),type(c),type(d))

# bool
a = True
b = False
c = a and b
d = a or b

print(type(a),type(b),type(c),type(d))

# String - (str)

a = 'apple'
b = "basket"
c = '''can i play with apple
and use it as a basketball'''
d = """hi
we 
are 
the 
string
"""

print(type(a),type(b),type(c),type(d))

# Nonetype - None

a = None
b = None
print(type(a),type(b))
z = None
print(z)

# data - structure

# list -> square brackets
a = [1,2,3,4,5,6]
print(type(a))

# tuple -> round brackets
a = (1,2,3,4,5,6)
b = 1,4,5,6,3
print(type(a),type(b))

# set -> curly braces
a = {1,2,3,4,5,6}
b = {1,4,5,6,3,1,2,3,3,2,2,2,2,1,21,1}
print(type(a), type(b))

# dict -> curly braces
d = {"name":'apple','price':200}
c = {1:1000,2:2000,3:3000}
print(type(c), type(d))

# programmatically check type -

a = 10
out = isinstance(a, int)
print("is a an integer =>",out)
out = isinstance(a, float)
print("is a float =>",out)

price = input('enter the price of mouse you bought:')
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,str))

# whatever you give as input is always a string, until u change the datatype 