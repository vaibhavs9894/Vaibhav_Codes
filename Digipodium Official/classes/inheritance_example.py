class Animal:
    is_alive = True
    
    def eat_food(self, food):
        print('animal eats',food)

# inheritance
class Vertebrate(Animal):
    has_spine =True

# inheritance level 2
class Bird(Vertebrate):
    has_wings = True

    def fly(self):
        print('bird is flying')

if __name__ == "__main__":
    a = Animal()
    a.eat_food('plant')
    a.eat_food('fish')
    print('living',a.is_alive)

    b = Vertebrate()
    b.eat_food('plant')
    b.eat_food('meat')
    print('living',b.is_alive)
    print('spine',b.has_spine)

    c = Bird()
    c.eat_food('worms')
    c.fly()
    c.eat_food('worms')
    c.fly()
    print("spine",c.has_spine)
    print("wings",c.has_wings)
    print("alive",c.is_alive)


    # cmd
    'git config --global user.name apnaname'
    'git config --global user.email apnaemail'