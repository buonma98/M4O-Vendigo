# Class: Inventory
# Purpose: Keep track of the products inside the vending machine.

# Create a class called Inventory.
class Inventory:

    # This function runs when a new inventory is created.
    def __init__(self):

        # Create an empty list to store our products.
        self.products = []

    # This function adds a product to the inventory.
    def add_product(self, product):

        # Add the product to our list.
        self.products.append(product)

    # This function checks which products are available.
    def get_available_products(self):

        # Return only products that have at least one unit in stock.
        return [product for product in self.products if product.stock > 0]
