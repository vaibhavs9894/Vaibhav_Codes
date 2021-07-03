rows = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < rows:
    k = 2 * rows - 2  
    for i in range(0, rows):  
 
        for j in range(0, k):  
         print(end=" ")  
    
        k = k - 1  
        for j in range(0, i + 1):  
            print(n1," ", end="") 
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1 
        print("")    
       
k = rows - 2
 
for i in range(rows, -1, -1):  
    
    for j in range(k, 0, -1):  
        print(end=" ")  
  
    k = k + 1  
    
    for j in range(0, i + 1):  
        print(n1," ", end="") 
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1 
    print("")       
       
    
    