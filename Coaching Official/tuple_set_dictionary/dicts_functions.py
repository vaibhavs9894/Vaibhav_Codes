# function
    # update
    # pop
    # popitem
    # get
    # keys
    # values
    # items
    # clear

fruits= {'apple':100,'banana':40,
         'cherry':150,'dragonfruit':200}

print('updating values in dict')

new_fruits = {'gauva':35,'peach':80}
fruits.update(new_fruits)
print(fruits)

print('removing values from dict')

fruits.pop('cherry')
print(fruits)

# better version
if 'orange' in fruits:
    fruits.pop('orange')
    print(fruits)
else:
    print('orange not found')

last_item_removed = fruits.popitem()
print(fruits)
print(f'{last_item_removed} removed from fruits')


# accessing value from dict
print(fruits['apple'])
# error => print(fruits['Apple']) 

# better version to access value from dict
print('using the get method in dict')
print(fruits.get('apple'))
print(fruits.get('Apple'))

print('using the get() with default value, in dict ')
print(fruits.get('Apple','price not found'))
print(fruits.get('banana','price not found'))

# accessing keys, values and pair wise items in dict
print(fruits.values())
print(fruits.keys())
print(fruits.items())

print('looping in dict')
print('=>normal loop get only keys')

for i in fruits:
    print(i)

print('=>get only values')
for i in fruits.values():
    print(i)

# another way to get values
# for i in fruits:
#     print(fruits[i])

print('=>get both key and value')
for k,v in fruits.items():
    print(k,'-->',v)

# print('=>get both key and value')
# for i in fruits:
#     print(i,'-->',fruits[i])