# replace is useful to replace data with something else in strings
msg = 'Brandon Sanderson is an American author of epic fantasy and science fiction'

umsg = msg.replace('author','writer')
print(umsg)

amsg = msg.replace('and','or')
print(amsg)

# remove something
fmsg = msg.replace('American','')
print(fmsg)