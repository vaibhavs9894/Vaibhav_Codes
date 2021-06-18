a = input("enter a number:")
b = input("enter another number:")

if a.isnumeric() and b.isnumeric():
    a = int(a)
    b = int(b)
    if a > b:
        print(a + b)
    else:
        print(a - b)
else:
    print("we need numbers not anything else")