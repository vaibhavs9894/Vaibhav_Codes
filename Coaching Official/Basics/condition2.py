name = input('enter ur name:')
percentage = input('enter percentage ')

if len(name)>0:
    print('you are called',name)

per = float(percentage) # type conversion
if per > 60:
    print("Wow, how could you do this")

if 60 < percentage:
    print('badiya h')