x = [0,1]
size = int(input('enter size of fibonacci series>> '))
for i in range(size):
    val = x[-1] + x[-2]
    x.append(val)

print(x)