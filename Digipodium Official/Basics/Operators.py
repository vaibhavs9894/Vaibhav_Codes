# operator
# mathematical
a = 10
b = 3
c = a + b
print("add output",c)

c = a - b
print("subs output",c)

c = a * b
print("mul output",c)

c = a ** b  
print("exponent output",c)

c = a / b  
print("division output",c)

c = a // b  # rounds of the division result
print("int division output",c)

c = a % b  # rounds of the division result
print("remainder output",c)

# comparison
x = 23
name = 'oli'

out = x > 15
print('x > 15',out)

out = x < 15
print('x < 15',out)

out = x == 25
print('x == 25',out)

out = x >= 25
print('x >= 25',out)

out = x <= 25
print('x <= 25',out)

out = x != 23
print('x != 23',out)

out = name == 'oli'
print("name == 'oli'",out)

out = name == 'oliphant'
print("name == 'oli'",out)

# logical
a = 11
b = 5
c = 7

out = a > b and b < 10
print('a > b and b < 10',out)

out = a > b or b > c
print('a > b and b > c',out)

out = name == 'moli' or name == 'oli'
print("name == 'moli' or name == 'oli'",out)

out = not a > 50
print("not a > 50",out)

out = not len(name) >= 5
print("not len(name) >= 5 ",out)

# membership - in
fruits = ['apple','banana','cherry','dragon fruit']

out = 'apricot' in fruits
print("'apricot' in fruits",out)

out = 'banana' in fruits
print("'banana' in fruits",out)

out = 'dragonfruit' in fruits
print("'dragonfruit' in fruits",out)

out = 'Apple' in fruits
print("'Apple' in fruits",out)


# instance or identity - is
# ask me about this in list
# combination 

a = 10
# a = a + 10
a += 10 # add 10 to the value of a
print("a += 10",a)

a -= 3 # subtract 3 from a
print("a -= 3",a)

a *= 2 # mul 2 with a
print("a *= 2",a)

a /= 2 # div 2 with a
print("a /= 2",a)

a **= 10 # a
print("a **= 10",a) 