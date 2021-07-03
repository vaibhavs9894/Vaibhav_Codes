a = 0
b = 1
print("    ",a,"\n   ",b)
rows = 3 
  
k = 2 * rows - 2  

for i in range(0, rows):  
     
    for j in range(0, k):  
        print(end=" ")  
     
    k = k - 1  
    
    for j in range(0, i + 1):  
        for i in range(2):
            c = a + b
                         
            print(c,end=' ')
            a = b
            b = c
        
    print("")  
   
k = rows - 2  

for i in range(rows, -1, -1):  
    
    for j in range(k, 0, -1):  
        print(end=" ")  
    
    k = k + 1  
     
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  