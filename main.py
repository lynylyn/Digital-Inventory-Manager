class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount):
        if self.quantity + amount >= 0:
            self.quantity += amount
        else:
            print("The quantity given was invalid.")

    def get_total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"ID: {self.product_id} | {self.name} | ${self.price} | Stock: {self.quantity}"

class Inventory:
    def __init__(self, products):
        self.products = {}

    def add_product(self, product):
        self.products[product_id].update_stock(amount)

    def display_all(self):
        for product in self.products.values():
            print(product)

if __name__ == "__main__":
    print("Welcome to the Inventory Manager.")
    print("\n(1) Add New Product\n(2) View All Inventory\n(3) Update Product Stock (Buy/Sell)\n(4) Exit\n")

    choice = input("Choose: ")

    if choice == "1":
        name = input("\nPlease enter the name of the product you'd like to add: ")
        product_id = input("\nPlease enter the id of the product: ")
        price = float(input("\nPlease enter the price of the product: "))
        quantity = int(input("\nPlease enter the quantity of the product: "))

        product = Product(product_id, name, price, quantity)
        Inventory.add_product(product)
        print("\nAdded successfully.")

    if choice == "2":
        Inventory.display_all()
        print("\nCompleted.")

    if input == "3":
        product_id = input("\nEnter product ID: ")
        amount = int(input("\n Enter the amount you'd like to update the stock by: "))
        Product.update_stock(product_id, amount)

    if input == "4":
        print("Exiting...")
        break

    else:
        print("The selection was invalid.")