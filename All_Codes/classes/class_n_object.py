# example of a simple class
class FoodItem:
    pass

# properties and behaviour
class Cat:
    # property -> class variable
    breed = 'persian'

class Product:
    # method -> class method -> used directly with class
    def help():
        print('this is class under contruction') 
###########creation object############
# object = Classname()

maggi = FoodItem()
roti = FoodItem()
name = 'ajay'
print(type(name))
print(type(maggi))

billu = Cat()
tommy = Cat()
print(billu, tommy)
print(billu.breed)
print(tommy.breed)

keyboard = Product()
monitor = Product()
# class function
Product.help()
# should not be used by object
# keyboard.help()
# monitor.help()