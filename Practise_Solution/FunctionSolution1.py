#Write a Function to calculate area and perimeter of rectangle. 
def area_rectangle(a,b):
    area= a*b
    print('area of reactangle is',area)

def Perimeter_Rectangle(a,b):
    p=2*(a+b)
    print('Perimeter of rectangle is',p)

area_rectangle(4,6)
Perimeter_Rectangle(3,9)
#------------------------------------------------------------------------------------------------------------------------------------
### Write a function to calculate area and circumference of a circle
def area_Circle(r):
    area=3.14*r*r
    print('Area of circle is',area)

def Circumference_Circle(r):
    c=2*3.14*r
    print('Circumference of Circle is',c)

area_Circle(12)
Circumference_Circle(22)
#------------------------------------------------------------------------------------------------------------------------------------
### Write a function to tell user if he/she is able to vote or not.`( Consider minimum age of voting to be 18. )

def Vote_elligible(a):
    if a == 18 or a > 18:
        print('Congrats!you are elligible to vote')
    else:
        print('Nah! You cant vote')

Vote_elligible(14)
Vote_elligible(23)        

