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

    # This function finds a specific product by its name.
    def findProduct(self, name):

        # Look through every product in our inventory.
        for product in self.products:

            # Check if the product's name matches what we're looking for.
            # lower() means capital letters won't matter.
            if product.name.lower() == name.lower():

                # We found the product!
                return product

        # If we checked everything and didn't find it, return nothing.
        return None

    # This function handles removing a product when purchased.
    def purchase_product(self, product):

        # First, make sure this product is actually in our inventory.
        if product not in self.products:

            # The product doesn't belong to our vending machine.
            return False

        # Ask the Product class to remove one from its stock.
        # It will also check whether any are left.
        return product.reduceStock()
