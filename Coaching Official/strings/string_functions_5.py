# split and join
msg = 'Brandon Sanderson is an American author of epic fantasy and science fiction'
msg2 = 'i was eating food. the food was cold. then i lived happily ever after'

words = msg.split()
print(words)
print(len(words))

# decide the character or substr to split from
words2 = msg2.split('.')
print(words2)
print(len(words2))

# decide number of maxsplits
msg = "apple,banana,pasta,cheese,butter,mango"
words = msg.split(',',3)
print(words)

# decide number of maxsplits in reversed order
msg = "apple,banana,pasta,cheese,butter,mango"
words = msg.rsplit(',',3)
print(words)