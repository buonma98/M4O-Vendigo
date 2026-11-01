"""
# product.py
# MobileMiniMart - Smart Vending Machine
# Model class representing an individual snack or beverage product
# Team: M4O | Author: Mary Buoni
"""

class Product:
    """
    Represents an individual snack or beverage product in the vending machine.

    Parameters:
    ----------
    name : str
        The display name of the item (e.g., 'Chips', 'Soda').
    price : float
        The cost of the product in USD (e.g., 1.50).
    stock : int
        The quantity of this product currently available in the machine.

    Examples:
    ---------
    1. Create a bag of chips with price $1.50 and stock of 5:
       >>> snack = Product("Chips", 1.50, 5)
       >>> snack.isAvailable()
       True
    """

    def __init__(self, name: str, price: float, stock: int):
        """
        Initialize a new Product instance with name, price, and stock quantity.
        """
        # Save the name of the product (example: "Chips")
        self.name = name

        # Save the price of the product (example: 1.50)
        self.price = price

        # Save how many units are available (example: 3)
        self.stock = stock

    def isAvailable(self) -> bool:
        """
        Check if the product is currently in stock.

        Returns:
        -------
        bool: True if stock is greater than 0, False if sold out.
        """
        # If stock is greater than zero, the product is available
        return self.stock > 0

    def reduceStock(self) -> bool:
        """
        Safely decrement the stock count by 1 when a customer makes a purchase.

        Returns:
        -------
        bool: True if stock was reduced successfully, False if already sold out.
        """
        # First, check if we have any units left
        if self.isAvailable():
            # Subtract one from current stock
            self.stock -= 1
            # Return True because the reduction succeeded
            return True

        # Return False because the product is sold out
        return False


if __name__ == "__main__":
    print("--- Running Product Class Verification Tests ---")

    # 1. Test product creation
    snack = Product("Chips", 1.50, 2)
    assert snack.name == "Chips", f"Expected 'Chips', got {snack.name}"
    assert snack.price == 1.50, f"Expected 1.50, got {snack.price}"
    assert snack.stock == 2, f"Expected 2, got {snack.stock}"
    assert snack.isAvailable() is True, "Product with stock 2 should be available"
    print(f"[PASS] Product creation: {snack.name} (${snack.price:.2f}, Stock: {snack.stock})")

    # 2. Test first stock reduction (stock goes from 2 to 1)
    purchase_1 = snack.reduceStock()
    assert purchase_1 is True, "First reduction should succeed"
    assert snack.stock == 1, f"Expected stock 1, got {snack.stock}"
    assert snack.isAvailable() is True, "Product with stock 1 should still be available"
    print(f"[PASS] First purchase: stock reduced to {snack.stock}")

    # 3. Test second stock reduction (stock goes from 1 to 0)
    purchase_2 = snack.reduceStock()
    assert purchase_2 is True, "Second reduction should succeed"
    assert snack.stock == 0, f"Expected stock 0, got {snack.stock}"
    assert snack.isAvailable() is False, "Product with stock 0 should NOT be available"
    print(f"[PASS] Second purchase: stock reduced to {snack.stock} (now sold out)")

    # 4. Test purchase attempt when sold out (stock should remain 0)
    purchase_3 = snack.reduceStock()
    assert purchase_3 is False, "Reduction when sold out should return False"
    assert snack.stock == 0, f"Expected stock to remain 0, got {snack.stock}"
    print(f"[PASS] Attempted purchase while sold out: correctly returned {purchase_3}")

    print("--- All Product Assertions Passed Successfully! ---\n")
