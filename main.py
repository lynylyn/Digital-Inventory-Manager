class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount):
        if self.quantity + amount < 0:
            print("The quantity given was invalid.")
        else:
            self.quantity.append(self.quantity + amount)
            return self.quantity

    def get_total_value(self):
        total_value = self.price * self.quantity
        return total_value

    def __str__(self):
        return f"The total value for your order of {self.quantity} {self.name}/s was {self.get_total_value}."

class Inventory:
    def __init__(self, products):
        self.products = products
        products = {Product.product_id: Product.name}

    def add_product(self, product_id, name):
        self.products.update({product_id: name})

    def display_all(self):
        for product in self.products:
            Product.__str__(product)

#if __name__ == "__main__":
    #print("Welcome to the Inventory Manager.")
    #input = input("\n(1) Add New Product\n(2) View All Inventory\n(3) Update Product Stock (Buy/Sell)\n(4) Exit\n")
    #if input == "1":
        #name = input("Please enter the name of the product you'd like to add.")
        #product_id = input("Please enter the id of the product you'd like to add.")
        #Inventory.add_product(Inventory, product_id, name)
        #print("\nAdded successfully.")
    #if input == "2":
        #Inventory.display_all(Inventory)
        #print("\nCompleted.")
    #if input == "3":
        #amount = input("Please input the amount you'd like to update the stock by.")
        #Product.update_stock(Product, amount)
    #if input == "4":
        #exit
    #else:
        #print("The selection was invalid.")

object = Product(12, "car", 500, 2)
print(Product.__str__(object))