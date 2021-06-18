class Product:

    # constructor
    def __init__(self,title,price,category):
        self.title = title
        self.price = price
        self.category = category

    # instance function
    def get_discounted_price(self,discount = 10):
        disc_price = self.price * (discount/100)
        return self.price - disc_price


p1 = Product('wireless mouse',1200,'electonic')
p2 = Product('wireless mouse x1',3200,'electonic')

print(p1.title)
print('real price',p1.price)
print('discounted price',p1.get_discounted_price())
print('discounted price 5%',p1.get_discounted_price(5))
print('discounted price 50%',p1.get_discounted_price(50))

print(p2.title)
print('real price',p2.price)
print('discounted price',p2.get_discounted_price())
print('discounted price 25%',p2.get_discounted_price(25))