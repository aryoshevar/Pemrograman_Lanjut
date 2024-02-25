"""
Nama: Aryo Sheva Ramadhani
NIM: 215150307111009
Kelas: Pemrograman Lanjut-B
"""

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        return f"{self.product_id}. {self.name} - Price: ${self.price} - Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_products(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.display_info())
    
    def product_bought(self,name,quantity):
        quantity = int(quantity)
        for product in self.products:
            if name == product.name:
                if quantity <= product.quantity:
                    product.quantity -= quantity

class Customer:
    def __init__(self, credit):
        self.credit = credit
        self.cart_quantity = {}
        self.cart_price = 0
    
    def put_in_cart(self, name, quantity):
        quantity=int(quantity)
        for product in inventory.products:
            if name == product.name:
                quantity_is_valid = False
                temp = self.cart_quantity
                while not quantity_is_valid:
                    if name not in self.cart_quantity:
                        self.cart_quantity[name] = quantity
                        if self.cart_quantity[name] <= product.quantity:
                            quantity_is_valid = True
                        else:
                            print("Insufficient product quantity")
                            self.cart_quantity = temp
                    else:
                        self.cart_quantity[name] += quantity
                        if self.cart_quantity[name] <= product.quantity:
                            quantity_is_valid = True
                        else:
                            print("Insufficient product quantity")
                            self.cart_quantity = temp
                self.cart_price += (product.price * quantity)
                break

    def remove_from_cart(self, name, quantity):
        quantity = int(quantity)
        if len(self.cart_quantity) > 0:
            for product in inventory.products:
                if name == product.name:
                    quantity_is_valid = False
                    while not quantity_is_valid:
                        if quantity <= self.cart_quantity[name]:
                            self.cart_quantity[name] -= quantity
                            self.cart_price -= (product.price * quantity)
                            quantity_is_valid = True
                        else:
                            print("Insufficient product quantity")
                        if self.cart_quantity[name] == 0:
                            self.cart_quantity.pop(name)
                            break
        else:
            print("Your cart is empty")
    
    def display_cart(self):
        i = 1
        for name in self.cart_quantity:
            print(f"{i}. {name} - Quantity: {self.cart_quantity[name]}")
            i += 1
        print(f"Total Price = ${self.cart_price}")
    
    def checkout(self):
        if self.credit >= self.cart_price:
            for name in self.cart_quantity:
                inventory.product_bought(name,self.cart_quantity[name])
            return True
        else:
            print("Insufficient Credit")
            return False

def int_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        try:
            result = int(input(message).strip())
        except ValueError:
            print('Input must be a number')
        else:
            input_is_valid = True
    
    return str(result)

def float_input(message):
    input_is_valid = False
    result = ''
    while not input_is_valid:
        try:
            result = float(input(message).strip())
        except ValueError:
            print('Input must be a real number (e.g. 123.4567)')
        else:
            input_is_valid = True
    
    return str(result)
        
product1 = Product(1, 'Laptop', 599.99, 10)
product2 = Product(2, 'Smartphone', 299.99, 20)
product3 = Product(3, 'Mouse', 19.99, 50)

inventory = Inventory()
inventory.add_products(product1)
inventory.add_products(product2)
inventory.add_products(product3)

print("=====Welcome to Electronic Store=====")
balance = float_input("Your balance = $")
balance = float(balance)
customer = Customer(balance)

is_system_on = True
while(is_system_on):
    print("=====Welcome to Electronic Store=====")
    inventory.list_products()
    
    print()
    print(f"Your balance: {customer.credit}")
    print("Actions:")
    print("1. Buy product")
    print("2. Display your cart")
    print("3. Checkout/Exit")
    is_action = int_input("Choose Action:")
    is_action = int(is_action)

    if (is_action == 1):
        print("Which product would you like to buy?")
        input_is_valid = False
        while not input_is_valid:
            try:
                is_item = int_input("Choose Item:")
                is_item = int(is_item)
                id = is_item - 1
                it_name = inventory.products[id].name
                it_quantity = int_input(f"How many {it_name} would you like to buy?")
                it_quantity = int(it_quantity)
                customer.put_in_cart(it_name,it_quantity)
            except IndexError:
                print("Item not found")
            else:
                input_is_valid = True

    elif (is_action == 2):
        customer.display_cart()
        remove_is_valid = False
        while not remove_is_valid:
            is_remove = input("Do you want to remove item? (y/n) ")
            if (is_remove == 'y'):
                item_is_valid = False
                while not item_is_valid:
                    is_item = int_input("Choose Item:")
                    is_item = int(is_item)
                    if is_item <= len(customer.cart_quantity):
                        item_is_valid = True
                    else:
                        print("Item not found")
                id = is_item
                count = 1
                for item in customer.cart_quantity:
                    if (count == id):
                        it_name = item
                        item_is_valid = True
                    else:
                        count += 1
                it_quantity = int_input(f"How many {it_name} would you like to remove?")
                it_quantity = int(it_quantity)
                customer.remove_from_cart(it_name,it_quantity)
                remove_is_valid = True
            elif(is_remove == 'n'):
                remove_is_valid = True
            else:
                print("Input must be y or n")
        
    elif(is_action == 3):
        is_checkout = customer.checkout()
        if (is_checkout):
            customer.credit -= customer.cart_price
            print(f"Your remaining balance: ${customer.credit}")
            print("Checkout Success")
            inventory.list_products()
            is_system_on = False
        else:
            print("Checkout Failed")
    else:
        print("Action not found")

# Inimah projek akhir wkwkwk