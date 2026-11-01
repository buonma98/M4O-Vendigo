"""
# vending_machine.py
# MobileMiniMart - Smart Vending Machine
# Central controller class managing user interaction and business logic
# Team: M4O | Author: Mary Buoni
"""

from inventory import Inventory

class VendingMachine:
    """
    Main controller for the MobileMiniMart smart vending machine.
    Coordinates customer browsing, product selection, display updates,
    LED status calculations, and inventory stock management.

    Parameters:
    ----------
    inventory : Inventory
        The Inventory instance containing the stocked products.

    Examples:
    ---------
    1. Create a machine, browse, and purchase:
       >>> inv = Inventory()
       >>> vm = VendingMachine(inv)
       >>> vm.selectProduct()
    """

    def __init__(self, inventory: Inventory):
        """
        Initialize the VendingMachine with an Inventory instance
        and start product browsing at index 0.
        """
        # Connect our vending machine to its inventory
        self.inventory = inventory

        # Start by looking at the first product
        # Python starts counting at index 0 instead of 1
        self.selectedIndex = 0

    def browseProducts(self):
        """
        Advance to the next product in the inventory.
        If customer browses past the last item, wraps around back to the first.

        Returns:
        -------
        Product or None: The newly selected Product, or None if inventory is empty.
        """
        # First, check if our inventory is empty
        if not self.inventory.products:
            return None

        # Move to the next product in our list
        self.selectedIndex += 1

        # If we pass the last product, loop back to the first item (index 0)
        if self.selectedIndex >= len(self.inventory.products):
            self.selectedIndex = 0

        # Return the product we are now looking at
        return self.selectProduct()

    def selectProduct(self):
        """
        Retrieve the Product currently pointed to by selectedIndex.

        Returns:
        -------
        Product or None: The selected Product object, or None if inventory is empty.
        """
        # Check if we have any products
        if not self.inventory.products:
            return None

        # Find the product at our selected position
        return self.inventory.products[self.selectedIndex]

    def confirmPurchase(self) -> bool:
        """
        Process the customer's purchase request for the currently selected product.

        Returns:
        -------
        bool: True if purchase succeeded, False if product is sold out or unavailable.
        """
        # Find the product the customer selected
        product = self.selectProduct()

        # If there is no product, we cannot buy anything
        if product is None:
            return False

        # Try to remove one product from inventory
        if self.updateStock():
            # Update the displayed product information
            self.updateDisplay()
            # The purchase was successful!
            return True

        # The product is sold out
        return False

    def updateDisplay(self) -> tuple:
        """
        Prepare two formatted text lines for the 16x2 LCD screen.

        Returns:
        -------
        tuple[str, str]: (line1, line2) containing item name, price, and stock count.
        """
        # Find the currently selected product
        product = self.selectProduct()

        # If there are no products, show this default message
        if product is None:
            return ("No products", "Available")

        # Line 1 shows the product name and price formatted to 2 decimals
        line1 = f"{product.name} ${product.price:.2f}"

        # Line 2 shows how many units are currently left
        line2 = f"Stock: {product.stock}"

        # Return the two lines for the LCD screen to show
        return (line1, line2)

    def updateLEDStatus(self) -> str:
        """
        Determine the color status message for the LED lights based on stock:
        - 'Sold Out' (Red light) if stock is 0
        - 'Low Stock' (Yellow/Amber light) if stock is 1 or 2
        - 'Ready' (Green light) if stock is 3 or more

        Returns:
        -------
        str: Status string ('Ready', 'Low Stock', or 'Sold Out').
        """
        # Find the selected product
        product = self.selectProduct()

        # No product means nothing is available
        if product is None:
            return "Sold Out"

        # If stock is zero, the product is sold out
        if product.stock == 0:
            return "Sold Out"

        # If stock is 1 or 2, we are running low
        if product.stock <= 2:
            return "Low Stock"

        # Otherwise, we have plenty of products
        return "Ready"

    def updateStock(self) -> bool:
        """
        Deduct 1 unit of stock for the selected product via Inventory delegation.
        (Matches the 'upateStock' method in Mindy's UML diagram).

        Returns:
        -------
        bool: True if stock deduction succeeded, False otherwise.
        """
        # Find the product being purchased
        product = self.selectProduct()

        # If no product was selected, stop here
        if product is None:
            return False

        # Ask Inventory to process the purchase
        # Inventory then asks Product to remove one unit
        return self.inventory.purchase_product(product)


if __name__ == "__main__":
    print("--- Running VendingMachine Class Verification Tests ---")
    from product import Product

    # 1. Test empty vending machine handling
    empty_inv = Inventory()
    empty_vm = VendingMachine(empty_inv)
    assert empty_vm.selectProduct() is None, "Empty machine should select None"
    assert empty_vm.browseProducts() is None, "Empty machine browse should return None"
    assert empty_vm.confirmPurchase() is False, "Empty machine purchase should return False"
    assert empty_vm.updateDisplay() == ("No products", "Available"), "Display should show fallback"
    assert empty_vm.updateLEDStatus() == "Sold Out", "LED status should be Sold Out"
    print("[PASS] Empty inventory edge cases handled safely")

    # 2. Setup stocked machine
    inv = Inventory()
    p1 = Product("Pretzels", 1.25, 4)
    p2 = Product("Energy Drink", 2.50, 1)
    p3 = Product("Granola Bar", 1.00, 0)
    inv.add_product(p1)
    inv.add_product(p2)
    inv.add_product(p3)

    vm = VendingMachine(inv)

    # 3. Test initial selection (Index 0: Pretzels, stock 4)
    assert vm.selectedIndex == 0, f"Expected index 0, got {vm.selectedIndex}"
    assert vm.selectProduct() == p1, "Initial product should be Pretzels"
    assert vm.updateDisplay() == ("Pretzels $1.25", "Stock: 4")
    assert vm.updateLEDStatus() == "Ready", f"Expected 'Ready', got {vm.updateLEDStatus()}"
    print(f"[PASS] Initial item selected: {p1.name} (LED: {vm.updateLEDStatus()}, Display: {vm.updateDisplay()})")

    # 4. Test browsing (advance to Index 1: Energy Drink, stock 1)
    selected_2 = vm.browseProducts()
    assert vm.selectedIndex == 1, f"Expected index 1, got {vm.selectedIndex}"
    assert selected_2 == p2, "Browsed item should be Energy Drink"
    assert vm.updateDisplay() == ("Energy Drink $2.50", "Stock: 1")
    assert vm.updateLEDStatus() == "Low Stock", f"Expected 'Low Stock', got {vm.updateLEDStatus()}"
    print(f"[PASS] Browsed to item 2: {p2.name} (LED: {vm.updateLEDStatus()})")

    # 5. Test purchase confirmation (Energy Drink stock goes from 1 to 0)
    purchase_result = vm.confirmPurchase()
    assert purchase_result is True, "Purchase of Energy Drink should succeed"
    assert p2.stock == 0, f"Expected stock 0, got {p2.stock}"
    assert vm.updateDisplay() == ("Energy Drink $2.50", "Stock: 0")
    assert vm.updateLEDStatus() == "Sold Out", f"Expected 'Sold Out', got {vm.updateLEDStatus()}"
    print(f"[PASS] Purchase succeeded! Stock updated to {p2.stock}, LED changed to {vm.updateLEDStatus()}")

    # 6. Test browsing to Index 2 (Granola Bar, stock 0)
    selected_3 = vm.browseProducts()
    assert vm.selectedIndex == 2, f"Expected index 2, got {vm.selectedIndex}"
    assert selected_3 == p3, "Browsed item should be Granola Bar"
    assert vm.updateLEDStatus() == "Sold Out"
    # Attempting purchase on sold out item must fail
    assert vm.confirmPurchase() is False, "Purchase on sold out item must return False"
    print(f"[PASS] Browsed to sold-out {p3.name}: purchase correctly rejected")

    # 7. Test carousel wrap-around (browsing past index 2 wraps back to index 0)
    wrapped = vm.browseProducts()
    assert vm.selectedIndex == 0, f"Expected wrapped index 0, got {vm.selectedIndex}"
    assert wrapped == p1, "Carousel should wrap around to Pretzels"
    print(f"[PASS] Carousel wrap-around verified: wrapped back to {wrapped.name} at index 0")

    print("--- All VendingMachine Assertions Passed Successfully! ---\n")
