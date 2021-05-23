x = [23,2,13,12,43,56,12,876,97,89,23,34,5,343,2312]
a = ['alpha','beta','gamma']

idx_of_876 = x.index(876)
print('876 occurs at index',idx_of_876) 

idx_of_5 = x.index(5)
idx_of_12 = x.index(12)  # first occurance only 

print("5 occurs at",idx_of_5)
print("12 occurs at",idx_of_12)

# copy logic
b = a.copy()
print(a,b)

c = a # wrong way of copying a list
print(a,c)

print(a is b)
print(a is c) # true mean same memory location