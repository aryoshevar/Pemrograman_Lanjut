"""
Aryo Sheva Ramadhani 215150307111009
"""
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"{self.name} (Product ID: {self.product_id}) - Price: ${self.price} - Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.display_info())

product1 = Product(1, "Laptop", 999.99, 10)
product2 = Product(2, "Smartphone", 499.99, 20)
product3 = Product(3, "Mouse", 19.99, 50)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

print("List of products in the inventory:")
inventory.list_products()