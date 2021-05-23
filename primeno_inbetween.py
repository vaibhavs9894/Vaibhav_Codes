a=int(input('enter the no in between u want all prime no '))
b=int(input())
print(a,b)
for i in range(a,b):
    j=a-1
    if a%j==1:
        print(a)
        if j==1:
        break
    