x = [1,2,3,4,5]
colors = ['red','blue','green']
randomval = [29,83,12,10,9]

print("normal ->",x)
x.reverse()
print("reverse ->",x)
x.reverse()
print("back to normal ->",x)

print('normal',colors)
colors.sort()
print('alphabetical sort',colors)

randomval.sort()            # ascending order
print("sorted",randomval)

randomval.sort(reverse=True) # descending order
print("sorted",randomval)

# count function work the same as string count
y = [1,2,3,1,2,3,1,2,3,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,2,2,2,2,2,2,]
two_count = y.count(2)
three_count = y.count(3)
ten_count =y.count(10)

print('2 occurs =>',two_count)
print('3 occurs =>',three_count)
print('10 occurs =>',ten_count)