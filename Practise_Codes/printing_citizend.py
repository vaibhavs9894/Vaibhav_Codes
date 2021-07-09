class Citizen:

    def __init__(self, state, men, women, children):
        self.state = state
        self.men = men  
        self.women = women      
        self.children = children
        

    def show(self):  
        print("State  =>",self.state)
        print(" Men  =>",self.men)
        print("Women =>",self.women)
        print("Children =>",self.children)
    def __str__(self):
        return f"{self.state}   {self.men}{self.women}   {self.children}"
s1 = Citizen('Bihar',23500,17237,5927)
s2 = Citizen('Orissa',23658,24555,2364)
s3 = Citizen('U P',36517,22617,6314)
s4 = Citizen ('Jharkhand',23254,19845,1336)
s5 = Citizen('State','Men',' Women','Children')    
Citizen = [s1,s2,s3,s4,s5]

print('By Train \n ------- \n')
print(s5,'\n',s1,'\n',s2)

print('By Bus \n ------- \n')
print(s5,'\n',s3,'\n',s4)


