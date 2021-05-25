print('a Python program to get the Fibonacci series between 0 to 50.')
a = 0
b = 1
print(a,b,end=' ')
for i in range(50):
    c = a + b
    if c > 50:
        break
    print(c,end=' ')
    a = b
    b = c

print()
print('a Python program that accepts a word from the user and reverse it')

word = input('enter your word: ')

if len(word) >0:
    print(word,len(word))

for i in range(len(word)-1,-1,-1):
    print(word[i],end='')

# reverse word in python is actually
# word[::-1]