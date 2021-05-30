class Pet:
    
    # constructor
    def __init__(self, name, pettype, age):
        # instance variables (object variables)
        self.name = name
        self.pettype = pettype
        self.age = age



#################################

p1 = Pet('moti','dog',10)
p2 = Pet('kitkit','squirrel',1)
joey = Pet('joey','cat',1)
print(p1.name, p1.pettype, p1.age)
print(p2.name, p2.pettype, p2.age)
print(joey.name, joey.pettype, joey.age)

p1.age = 11 # you can change the properties after creation of objects
print(p1.name, p1.pettype, p1.age)