'''
Тут я ещё подумаю, списывать не хочу.


Heh
'''

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.stock = {}
        self.income = 0


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

if __name__ == '__main__':
    assert s.get_product_info('Ramen') == ('Ramen', 290)
