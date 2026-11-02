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

    Attributes:
    ----------
    products : list[Product]
        The list of Product objects currently stored in inventory.
    lowStockThreshold : int
        Quantity threshold below which an item is considered low stock (default: 2).

    Examples:
    ---------
    1. Create an inventory, add snacks, and check available:
       >>> inv = Inventory()
       >>> inv.addProduct(Product("Chips", 1.50, 3))
       >>> len(inv.getAvailableProducts())
       1
    """

    def __init__(self, lowStockThreshold: int = 2):
        """
        Initialize an empty Inventory with a fresh list for products
        and a configurable low-stock threshold.
        """
        # Create an empty list to store our products
        self.products = []

        # Threshold to flag an item as running low on stock
        self.lowStockThreshold = lowStockThreshold

    def addProduct(self, product: Product):
        """
        Add a new Product object to the inventory list.

        Parameters:
        ----------
        product : Product
            The product instance to add.
        """
        self.products.append(product)

    # Alias for backwards compatibility
    add_product = addProduct

    def getAvailableProducts(self) -> list:
        """
        Return a list containing only products that have at least one unit in stock.

        Returns:
        -------
        list[Product]: Filtered list of Product objects with stock > 0.
        """
        return [product for product in self.products if product.isAvailable()]

    # Alias for backwards compatibility
    get_available_products = getAvailableProducts

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
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def purchaseProduct(self, product: Product) -> bool:
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
        if product not in self.products:
            return False

        return product.reduceStock()

    # Alias for backwards compatibility
    purchase_product = purchaseProduct


if __name__ == "__main__":
    print("--- Running Inventory Class Verification Tests ---")

    # 1. Test empty inventory initialization
    inv = Inventory()
    assert len(inv.products) == 0, f"Expected 0 products, got {len(inv.products)}"
    assert len(inv.getAvailableProducts()) == 0, "Available products should be empty"
    assert inv.lowStockThreshold == 2, f"Expected lowStockThreshold 2, got {inv.lowStockThreshold}"
    print("[PASS] Empty inventory initialized successfully with lowStockThreshold = 2")

    # 2. Test adding products (both camelCase and snake_case)
    p1 = Product("Chips", 1.50, 3)
    p2 = Product("Soda", 2.00, 1)
    p3 = Product("Candy", 1.00, 0)
    inv.addProduct(p1)
    inv.add_product(p2)
    inv.addProduct(p3)
    assert len(inv.products) == 3, f"Expected 3 products, got {len(inv.products)}"
    print(f"[PASS] Added 3 products: {[p.name for p in inv.products]}")

    # 3. Test getAvailableProducts (only p1 and p2 have stock > 0)
    available = inv.getAvailableProducts()
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

    # 5. Test purchaseProduct delegation
    assert inv.purchaseProduct(p2) is True, "Purchase of Soda should succeed"
    assert p2.stock == 0, f"Expected Soda stock 0, got {p2.stock}"
    assert inv.purchaseProduct(p2) is False, "Second purchase of Soda should fail (out of stock)"
    print("[PASS] Purchase product successfully delegated to Product.reduceStock()")

    # 6. Test purchasing an external product not in this inventory
    foreign_product = Product("Gum", 0.50, 5)
    assert inv.purchaseProduct(foreign_product) is False, "Purchasing foreign product should return False"
    print("[PASS] Foreign product rejection verified")

    print("--- All Inventory Assertions Passed Successfully! ---\n")
