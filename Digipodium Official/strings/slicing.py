name ='Vijay Deenanath Chauhan'

fname = name[0:5] # vijay
print(fname)
mname = name[6:15] # Deenanath
print(mname)
mname = name[6:-8] # Deenanath
print(mname)
lname = name[-7:len(name)]
print(lname)

# better version of fname and lname slices
fname = name[:5] # skip 0 when starting from begining
lname = name[-7:] # skip len() if ending on last 
print(fname,lname)

# fullname
print(name[:])

# reverse the name
print(name[::-1])

# every 2 second char in string
print(name[::2])