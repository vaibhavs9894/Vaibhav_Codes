a = 0
b = 1
m=" "
print(a,b,end=' ')
for i in range(7):
    c = a + b
    print(m*b,c,end='\n ')
    a = b
    b = c
