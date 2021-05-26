name = "Alexis" # outside function

def who():
    print('who am i ?')
    print(f'i am {name}')  # can be access inside function

def what():
    print('what are you?')
    name = 'God king'      # python cannot change the value of variable created outside directly
    print(f'I am {name}')  # this is just the local value of name variable

def update_name():
    global name            # this keyword tells python, that we want to use global variable and also modify value
    print('old name',name)
    name = "Alexander"     # this line updates the global variable now
    print('new name',name)


who()
print('global variable =>',name)
what()
print('global variable =>',name)
update_name()
print('global variable =>',name)