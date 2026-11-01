# Purpose: Control the main actions of our vending machine.

# Create a class called VendingMachine.
class VendingMachine:

    # This function runs when the vending machine is created.
    def __init__(self, inventory):

        # Connect our vending machine to its inventory.
        self.inventory = inventory

        # Start by looking at the first product.
        # Python starts counting at 0 instead of 1.
        self.selectedIndex = 0

    # This function lets customers browse products.
    def browseProducts(self):

        # First, check if our inventory is empty.
        if not self.inventory.products:
            return None

        # Move to the next product in our list.
        self.selectedIndex += 1

        # If we pass the last product, go back to the first.
        if self.selectedIndex >= len(self.inventory.products):
            self.selectedIndex = 0

        # Return the product we're now looking at.
        return self.selectProduct()

    # This function selects the current product.
    def selectProduct(self):

        # Check if we have any products.
        if not self.inventory.products:
            return None

        # Find the product at our selected position.
        return self.inventory.products[self.selectedIndex]

    # This function confirms a customer's purchase.
    def confirmPurchase(self):

        # Find the product the customer selected.
        product = self.selectProduct()

        # If there is no product, we cannot buy anything.
        if product is None:
            return False

        # Try to remove one product from inventory.
        if self.updateStock():

            # Update the displayed product information.
            self.updateDisplay()

            # The purchase was successful!
            return True

        # The product is sold out.
        return False

    # This function prepares information for the LCD screen.
    def updateDisplay(self):

        # Find the currently selected product.
        product = self.selectProduct()

        # If there are no products, show this message.
        if product is None:
            return ("No products", "Available")

        # Line 1 shows the name and price.
        line1 = f"{product.name} ${product.price:.2f}"

        # Line 2 shows how many are left.
        line2 = f"Stock: {product.stock}"

        # Return the two lines for the LCD to show later.
        return (line1, line2)

    # This function decides what the LED lights should show.
    def updateLEDStatus(self):

        # Find the selected product.
        product = self.selectProduct()

        # No product means nothing is available.
        if product is None:
            return "Sold Out"

        # If stock is zero, the product is sold out.
        if product.stock == 0:
            return "Sold Out"

        # If stock is 1 or 2, we're running low.
        if product.stock <= 2:
            return "Low Stock"

        # Otherwise, we have enough products.
        return "Ready"

    # This function updates stock after a purchase.
    def updateStock(self):

        # Find the product being purchased.
        product = self.selectProduct()

        # If no product was selected, stop here.
        if product is None:
            return False

        # Ask Inventory to process the purchase.
        # Inventory then asks Product to remove one unit.
        return self.inventory.purchase_product(product)
