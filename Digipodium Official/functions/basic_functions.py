# function 1- takes no argument
def hello():
    '''
    this is a very serious function
    '''
    print('hello frds, chai peelo')

hello()
hello()

for i in range(10):
    hello()

def world():
    print('this is an awesome function')
    hello()
    print('now you are also awesome')

world()

def divide():
    '''
    taking input inside a function is super stupid, but u can still do it
    '''
    x =  int(input('enter a number: '))
    y = int(input('enter another number: '))
    print(x/y)

divide()