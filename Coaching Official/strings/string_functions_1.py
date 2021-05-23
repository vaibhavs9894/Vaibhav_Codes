msg  = "This is an Example Message from myself"

print(msg)
# upper case - for just printing output
print(msg.upper())

# upper case - and putting it in a variable
msg_upper = msg.upper()
print(msg_upper)

print(msg.lower())
print(msg.capitalize())
print(msg.swapcase())
print(msg.title())

word ='Apple'
word2 = 'APPLE'
if word.upper() == word2:
    print('apples')