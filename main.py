from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Banane", 700, 8)
p2 = Product("Pere", 200, 10)
p3 = Product("Portocale", 150, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

