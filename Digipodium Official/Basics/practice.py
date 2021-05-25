#1Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

for i in range(1500,2701):
    if i%7==0 and i%5==0:
       print(i)
  
#2Write a Python program to count the number of even and odd numbers from a series of numbers.
a={23,2,58,56,6,7,4,9,65}
evencnt=0
oddcnt=0
for i in a:
    if i%2==0:
      evencnt += 1
    else:
      oddcnt += 1
print('Total Even no are',evencnt)
print('Total Odd no are',oddcnt)

#3Write a Python program to get the Fibonacci series between 0 to 50.
a=0
b=1
print('Fibonacci series from 0 to 50 is')
print(a, b,end=" ")
c=0 
while c<51: 
    c =a+b
    a=b
    b=c
    print(c,end=" ")

#4Write a Python program that accepts a word from the user and reverse it.
a=str(input('enter a String'))
b=''
for char in a:
    print(char)
    b=char + b
print('reverse of string is',b)