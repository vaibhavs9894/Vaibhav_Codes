  
# 7 -> 7/2, 7/3, 7/4 ,7/5 ,7/6  prime
# 20 -> 20/2  non prime

# program to find if number is prime
num = int(input('enter a number : '))

# for-else => we can use it to find if our loop has completed all iterations successfully

for i in range(2, num):
    print(num,'%',i,'=',num % i)
    if num % i ==0:
        print('non prime')
        break
else:
    print('prime')

# time complexity can be reduced here