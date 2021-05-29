### Write a function to find factorial of a number but also store the factorials calculated in a dictionary as 
#   done in the Fibonacci series example.

def factorial(a):
    f=1
    for i in range(1,a+1):
        f = f*i
    print('Factorial of',a,'is',f)
    return f

factorial(7)
fact = {}
print('Factorial of no from 10 to 100')
for i in range(10,100):
    m=factorial(i)
    fact[i]= m
print(fact)