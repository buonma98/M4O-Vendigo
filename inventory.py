"""
# inventory.py
# MobileMiniMart - Smart Vending Machine
# Container class managing the collection of stocked products
# Team: M4O | Author: Mary Buoni
"""

from product import Product

class Inventory:
    """
    Manages the collection of all products stocked in the vending machine.

    Parameters:
    ----------
    None

    Examples:
    ---------
    1. Create an inventory and add snacks:
       >>> inv = Inventory()
       >>> inv.add_product(Product("Chips", 1.50, 3))
       >>> len(inv.get_available_products())
       1
    """

    def __init__(self):
        """
        Initialize an empty Inventory with a fresh list for products.
        """
        # Create an empty list to store our products
        self.products = []

    def add_product(self, product: Product):
        """
        Add a new Product object to the inventory list.

        Parameters:
        ----------
        product : Product
            The product instance to add.
        """
        # Add the product to our list
        self.products.append(product)

    def get_available_products(self) -> list:
        """
        Return a list containing only products that have at least one unit in stock.

        Returns:
        -------
        list: Filtered list of Product objects with stock > 0.
        """
        # Return only products that are currently available (stock > 0)
        return [product for product in self.products if product.isAvailable()]

    def findProduct(self, name: str):
        """
        Find a specific product by its name using a case-insensitive match.

        Parameters:
        ----------
        name : str
            The name of the snack to search for (e.g., 'chips', 'Chips').

        Returns:
        -------
        Product or None: The matching Product object, or None if not found.
        """
        # Look through every product in our inventory
        for product in self.products:
            # Check if the product's name matches what we're looking for (ignoring case)
            if product.name.lower() == name.lower():
                # We found the product!
                return product

        # If we checked everything and didn't find it, return None
        return None

    def purchase_product(self, product: Product) -> bool:
        """
        Process the sale of a product by verifying inventory membership
        and calling the Product's reduceStock() method.

        Parameters:
        ----------
        product : Product
            The product being purchased.

        Returns:
        -------
        bool: True if purchase succeeded, False if product is invalid or sold out.
        """
        # First, make sure this product is actually in our inventory
        if product not in self.products:
            # The product doesn't belong to our vending machine
            return False

        # Ask the Product class to remove one from its stock
        # It will also check whether any units are left
        return product.reduceStock()


if __name__ == "__main__":
    print("--- Running Inventory Class Verification Tests ---")

    # 1. Test empty inventory initialization
    inv = Inventory()
    assert len(inv.products) == 0, f"Expected 0 products, got {len(inv.products)}"
    assert len(inv.get_available_products()) == 0, "Available products should be empty"
    print("[PASS] Empty inventory initialized successfully")

    # 2. Test adding products
    p1 = Product("Chips", 1.50, 3)
    p2 = Product("Soda", 2.00, 1)
    p3 = Product("Candy", 1.00, 0)
    inv.add_product(p1)
    inv.add_product(p2)
    inv.add_product(p3)
    assert len(inv.products) == 3, f"Expected 3 products, got {len(inv.products)}"
    print(f"[PASS] Added 3 products: {[p.name for p in inv.products]}")

    # 3. Test get_available_products (only p1 and p2 have stock > 0)
    available = inv.get_available_products()
    assert len(available) == 2, f"Expected 2 available products, got {len(available)}"
    assert p1 in available, "Chips should be in available list"
    assert p2 in available, "Soda should be in available list"
    assert p3 not in available, "Candy (stock 0) should NOT be in available list"
    print(f"[PASS] Available products filtered correctly: {[p.name for p in available]}")

    # 4. Test findProduct (case-insensitive search)
    assert inv.findProduct("chips") == p1, "Search for 'chips' failed"
    assert inv.findProduct("SODA") == p2, "Search for 'SODA' failed"
    assert inv.findProduct("Water") is None, "Search for unstocked 'Water' should return None"
    print("[PASS] Case-insensitive findProduct succeeded for lowercase, uppercase, and missing items")

    # 5. Test purchase_product delegation
    assert inv.purchase_product(p2) is True, "Purchase of Soda should succeed"
    assert p2.stock == 0, f"Expected Soda stock 0, got {p2.stock}"
    assert inv.purchase_product(p2) is False, "Second purchase of Soda should fail (out of stock)"
    print("[PASS] Purchase product successfully delegated to Product.reduceStock()")

    # 6. Test purchasing an external product not in this inventory
    foreign_product = Product("Gum", 0.50, 5)
    assert inv.purchase_product(foreign_product) is False, "Purchasing foreign product should return False"
    print("[PASS] Foreign product rejection verified")

    print("--- All Inventory Assertions Passed Successfully! ---\n")
