from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Mere", 500, 5)
p2 = Product("Pere", 200, 10)
p3 = Product("Portocale", 150, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.show_products()
print("Total inventory value:", manager.total_value())

from cart import Cart

cart = Cart()

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

cart.show_cart()
print("Carttotal:", cart.total_price())