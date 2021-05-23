#Program for adding all the even value till the entered no.
sum = 0

a = input("enter a value ")

if (a%2)==0:
 for i in range(0,a,2):
      sum = sum + a
else:
 a= a-1    
 for i in range(0,a,2):
      sum = sum + a
      
print("The addition is :-",sum)       


