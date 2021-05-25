msg='Warren Edward Buffett is an American investor, business tycoon, philanthropist, and the chairman and CEO of Berkshire Hathaway'
#question1
k=['a','A','e','E','i','I','o','O','u','U']
for c in msg:
       if c in k:
          msg=msg.replace(c,'')

#question2
l=0
for c in msg:
       if c in k:
          l+=1
print('no of vowels in string is -->',l)
print(msg)