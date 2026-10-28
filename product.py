# Class: Product
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
