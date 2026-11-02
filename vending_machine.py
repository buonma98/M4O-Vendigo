"""
# vending_machine.py
# MobileMiniMart - Smart Vending Machine
# Central controller class managing user interaction, inventory, and mobility
# Team: M4O | Author: Mary Buoni
"""

from inventory import Inventory
from movement_controller import MovementController
from navigation_controller import NavigationController

class MobileVendingMachine:
    """
    Main controller for the MobileMiniMart smart mobile vending machine.
    Coordinates customer browsing, snack selection, display updates,
    LED status calculations, inventory stock management, and autonomous mobility.

    Attributes:
    ----------
    inventory : Inventory
        The Inventory instance containing the stocked products.
    lcd : LCD or None
        LCD display instance for rendering messages.
    knob : Knob or None
        Potentiometer knob for customer selection navigation.
    ledStrip : LEDStrip or None
        RGB status light strip instance.
    buzzer : Buzzer or None
        Audio buzzer instance for chime and error alerts.
    button : Button or None
        Purchase confirmation button instance.
    selectedIndex : int
        Index of the currently selected product (starts at 0).
    awaitingConfirmation : bool
        Flag indicating if a product is selected and awaiting customer confirmation (default: False).
    movementController : MovementController or None
        Dual-motor movement controller for driving and steering.
    navigationController : NavigationController or None
        Autonomous navigation brain for obstacle detection and self-driving.

    Examples:
    ---------
    1. Create a machine, browse, and purchase:
       >>> inv = Inventory()
       >>> vm = MobileVendingMachine(inv)
       >>> vm.selectProduct()
    """

    def __init__(self, inventory: Inventory, lcd=None, knob=None, ledStrip=None,
                 buzzer=None, button=None, selectedIndex: int = 0,
                 awaitingConfirmation: bool = False,
                 movementController: MovementController = None,
                 navigationController: NavigationController = None):
        """
        Initialize the MobileVendingMachine with its inventory, customer peripherals,
        and mobility controllers.
        """
        self.inventory = inventory
        self.lcd = lcd
        self.knob = knob
        self.ledStrip = ledStrip
        self.buzzer = buzzer
        self.button = button

        # Product selection index
        self.selectedIndex = selectedIndex

        # State flag for pending purchase confirmation
        self.awaitingConfirmation = awaitingConfirmation

        # Mobility and navigation systems
        self.movementController = movementController
        self.navigationController = navigationController

    def browseProducts(self):
        """
        Advance to the next product in the inventory.
        Wraps around to the first item if customer browses past the end.
        Sets awaitingConfirmation to True.

        Returns:
        -------
        Product or None: The newly selected Product, or None if inventory is empty.
        """
        if not self.inventory.products:
            return None

        self.selectedIndex += 1
        if self.selectedIndex >= len(self.inventory.products):
            self.selectedIndex = 0

        self.awaitingConfirmation = True
        return self.selectProduct()

    def selectProduct(self):
        """
        Retrieve the Product currently pointed to by selectedIndex.

        Returns:
        -------
        Product or None: The selected Product object, or None if inventory is empty.
        """
        if not self.inventory.products:
            return None

        return self.inventory.products[self.selectedIndex]

    def confirmPurchase(self) -> bool:
        """
        Process the customer's purchase request for the currently selected product.
        Resets awaitingConfirmation to False on completion.

        Returns:
        -------
        bool: True if purchase succeeded, False if product is sold out or unavailable.
        """
        product = self.selectProduct()
        if product is None:
            return False

        if self.updateStock():
            self.updateDisplay()
            self.awaitingConfirmation = False
            return True

        return False

    def updateDisplay(self) -> tuple:
        """
        Prepare two formatted text lines for the 16x2 LCD screen.

        Returns:
        -------
        tuple[str, str]: (line1, line2) containing item name, price, and stock count.
        """
        product = self.selectProduct()
        if product is None:
            return ("No products", "Available")

        line1 = f"{product.name} ${product.price:.2f}"
        line2 = f"Stock: {product.stock}"
        return (line1, line2)

    def updateLEDStatus(self) -> str:
        """
        Determine the color status message for the LED lights based on stock:
        - 'Sold Out' if stock is 0
        - 'Low Stock' if stock is at or below inventory.lowStockThreshold
        - 'Ready' if stock is abundant

        Returns:
        -------
        str: Status string ('Ready', 'Low Stock', or 'Sold Out').
        """
        product = self.selectProduct()
        if product is None or product.stock == 0:
            return "Sold Out"

        threshold = getattr(self.inventory, "lowStockThreshold", 2)
        if product.stock <= threshold:
            return "Low Stock"

        return "Ready"

    def updateStock(self) -> bool:
        """
        Deduct 1 unit of stock for the selected product via Inventory delegation.

        Returns:
        -------
        bool: True if stock deduction succeeded, False otherwise.
        """
        product = self.selectProduct()
        if product is None:
            return False

        # Support both purchaseProduct and purchase_product
        if hasattr(self.inventory, "purchaseProduct"):
            return self.inventory.purchaseProduct(product)
        return self.inventory.purchase_product(product)

    def startAutomaticDriving(self):
        """
        Engage autonomous driving mode via the NavigationController.
        """
        if self.navigationController is not None:
            print("[MobileVendingMachine] Engaging autonomous navigation...")
            self.navigationController.startAutomatic()
        elif self.movementController is not None:
            print("[MobileVendingMachine] Driving forward...")
            self.movementController.moveForward()

    def stopAutomaticDriving(self):
        """
        Disengage autonomous driving and halt all movement.
        """
        if self.navigationController is not None:
            print("[MobileVendingMachine] Disengaging autonomous navigation...")
            self.navigationController.stopAutomatic()
        elif self.movementController is not None:
            print("[MobileVendingMachine] Stopping movement...")
            self.movementController.stop()


# Alias for backwards compatibility
VendingMachine = MobileVendingMachine


if __name__ == "__main__":
    print("--- Running MobileVendingMachine Class Verification Tests ---")
    from product import Product

    # 1. Test empty machine handling
    empty_inv = Inventory()
    empty_vm = MobileVendingMachine(empty_inv)
    assert empty_vm.selectProduct() is None, "Empty machine should select None"
    assert empty_vm.browseProducts() is None, "Empty machine browse should return None"
    assert empty_vm.confirmPurchase() is False, "Empty machine purchase should return False"
    assert empty_vm.updateDisplay() == ("No products", "Available")
    assert empty_vm.updateLEDStatus() == "Sold Out"
    assert empty_vm.awaitingConfirmation is False
    print("[PASS] Empty inventory edge cases handled safely")

    # 2. Setup stocked machine with movement and navigation
    inv = Inventory()
    p1 = Product("Pretzels", 1.25, 4)
    p2 = Product("Energy Drink", 2.50, 1)
    p3 = Product("Granola Bar", 1.00, 0)
    inv.addProduct(p1)
    inv.addProduct(p2)
    inv.addProduct(p3)

    mc = MovementController()
    nc = NavigationController(movementController=mc)
    vm = MobileVendingMachine(inv, movementController=mc, navigationController=nc)

    # 3. Test initial selection
    assert vm.selectedIndex == 0
    assert vm.selectProduct() == p1
    assert vm.updateDisplay() == ("Pretzels $1.25", "Stock: 4")
    assert vm.updateLEDStatus() == "Ready"
    print(f"[PASS] Initial item selected: {p1.name} (LED: {vm.updateLEDStatus()})")

    # 4. Test browsing and awaitingConfirmation flag
    selected_2 = vm.browseProducts()
    assert vm.selectedIndex == 1
    assert selected_2 == p2
    assert vm.awaitingConfirmation is True, "awaitingConfirmation should be True after browsing"
    assert vm.updateLEDStatus() == "Low Stock"
    print(f"[PASS] Browsed to item 2: {p2.name} (awaitingConfirmation: {vm.awaitingConfirmation})")

    # 5. Test purchase confirmation
    purchase_result = vm.confirmPurchase()
    assert purchase_result is True, "Purchase should succeed"
    assert p2.stock == 0
    assert vm.awaitingConfirmation is False, "awaitingConfirmation should be False after purchase"
    assert vm.updateLEDStatus() == "Sold Out"
    print(f"[PASS] Purchase succeeded! Stock: {p2.stock}, awaitingConfirmation reset to {vm.awaitingConfirmation}")

    # 6. Test autonomous driving commands
    vm.startAutomaticDriving()
    assert nc.automaticMode is True, "NavigationController should be in automatic mode"
    vm.stopAutomaticDriving()
    assert nc.automaticMode is False, "NavigationController should be stopped"
    print("[PASS] Autonomous driving start and stop commands verified")

    print("--- All MobileVendingMachine Assertions Passed Successfully! ---\n")
