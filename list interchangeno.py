#WAp to interchange first and last digit of list
a=[1,2,3,4,5,6,7,8,9] 
print(a)
print(type(a))
l=a[0]
a[0]=a[-1]
a[-1]=l
print(a)