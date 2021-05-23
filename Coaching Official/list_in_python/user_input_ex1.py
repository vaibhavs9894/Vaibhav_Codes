# a program to create list from user input and then do some statisics

num = []                                                            # blank list
print("please enter 10 values below, one value at a time")          # simple message
for i in range(1,11):                                               # loop from 1 to 10                    
    val =  int(input(f'enter {i} >>'))                              # input function
    num.append(val)                                                 # append value to list

print("length of list",len(num))
print("sum of list",sum(num))
print("mean of list",sum(num)/len(num))
print("max value of list",max(num))
print("min value of list",min(num))