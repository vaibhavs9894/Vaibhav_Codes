fname = 'Vijay'
lname = 'Dixit'

# concatenation - joining strings together

fullname = fname + ' ' + lname + ' is the name'
print(fullname)

# duplication - cloning the string

word = 'ha'
print(word * 3)
print('-|-'* 2 )
print('/' * 25)

for i in range(1,10):
    print('$ ' * i)

# membership operator
message = 'the most important thing for a coder is to code'

if 'thing' in message:
    print('thing -> word found')

if 'very' in message:
    print('very -> word found')

if 'z' not in message:
    print('z is not available in message')

print('elephant' in message)