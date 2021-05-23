a = input('enter something:')
if a.isupper():
    print('a is upper')
if a.islower():
    print('a is lower')
if a.istitle():
    print('a is in title case')
if a.isalpha():
    print('a only contains alphabets')
if a.isalnum():
    print('a contains alphabets and numbers only')
if a.isnumeric():
    print('a contains numbers only')
if a.isspace():
    print('a only contains spaces')
if a.isprintable():
    print('a can be printed')
if a.isascii():
    print('is ascii character')
if a.isdigit():
    print('is contans digits only')
if a.isdecimal():
    print('is contans decimal only')

# check if input is float
b = input('enter a float')
if b.count('.') == 1 and  b.replace('.','').isnumeric():
    print("b is float")
else:
    print('b is not a float')