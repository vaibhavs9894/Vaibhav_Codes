#Addition of all even no in between
sum = 0

a =int(input("enter a no"))

if (a%2)==0:
   print("a is even")
else:
   print("a is odd")

for i in range(0,a,2):
      sum = sum + a
      print(i,"-->",sum)
      

print("The Addition is:-",sum)    

