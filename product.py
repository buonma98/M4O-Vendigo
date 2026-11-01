# Purpose: Store information about each snack in the vending machine.

# Create a class called Product to represent a snack.
class Product:

    # This function runs whenever a new product is created.
    # Each product must have a name, price, and stock quantity.
    def __init__(self, name, price, stock):

        # Save the name of the product (example: "Chips").
        self.name = name

        # Save the price of the product (example: 1.50).
        self.price = price

        # Save how many units are available (example: 3).
        self.stock = stock

    # This function checks if the product is available.
    def isAvailable(self):

        # If stock is greater than zero, the product is available.
        # Return True if available, or False if sold out.
        return self.stock > 0

    # This function removes one product after a purchase.
    def reduceStock(self):

        # First, check if we have any products left.
        if self.isAvailable():

            # Subtract one from the current stock.
            self.stock -= 1

            # Return True because the purchase was successful.
            return True

        # Return False because the product is sold out.
        return False
