"""
# button.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the physical purchase confirmation button
# Team: M4O | Author: Mary Buoni
"""

class Button:
    """
    Represents the physical push-button on the MobileMiniMart vending machine.
    Used by the customer to confirm their selection and finalize a snack purchase.

    NOTE: This is a starter class for our initial proposal.
    Physical hardware interfacing (Pico GPIO digital input with pull-up/pull-down resistor)
    will be implemented in Phase 2. For now, it provides a clean software structure
    to check press state and trigger purchase confirmation.

    Parameters:
    ----------
    vending_machine : VendingMachine, optional
        Reference to the VendingMachine controller to trigger confirmPurchase() on press.

    Examples:
    ---------
    1. Check button state and confirm purchase:
       >>> btn = Button()
       >>> btn.isPressed()
       False
    """

    def __init__(self, vending_machine=None):
        """
        Initialize the Button with an unpressed state and an optional
        reference to the VendingMachine controller.
        """
        # Tracks whether the physical button is currently being held down
        self.pressed = False

        # Optional link to the VendingMachine controller
        self.vending_machine = vending_machine

    def isPressed(self) -> bool:
        """
        Check if the button is currently pressed down.

        Returns:
        -------
        bool: True if pressed, False if unpressed/released.

        NOTE: This is a placeholder method. In Phase 2, this method will read
        the digital voltage level (0 or 1) from the Pico GPIO pin.
        """
        # Placeholder: Returns simulated press state
        return self.pressed

    def confirmPurchase(self) -> bool:
        """
        Trigger the purchase confirmation action associated with this button.
        If connected to a VendingMachine, it calls the machine's confirmPurchase() method.

        Returns:
        -------
        bool: True if purchase was successfully processed, False otherwise.
        """
        print("[Button] Button pressed: confirmPurchase() triggered")

        # If connected to a VendingMachine instance, delegate the purchase action
        if self.vending_machine is not None:
            return self.vending_machine.confirmPurchase()

        # Placeholder fallback if no vending machine is attached
        return True


if __name__ == "__main__":
    print("--- Running Button Class Verification Tests ---")

    # 1. Test standalone button
    btn = Button()
    assert btn.isPressed() is False, "Initial button state should be unpressed (False)"

    # Test simulated press
    btn.pressed = True
    assert btn.isPressed() is True, "Button should report pressed (True)"

    btn.pressed = False
    assert btn.isPressed() is False, "Button should report unpressed (False)"

    # Standalone confirmPurchase call
    result = btn.confirmPurchase()
    assert result is True, "Standalone confirmPurchase() should return True"
    print("[PASS] Standalone button state and action verified")

    # 2. Test button connected to VendingMachine
    from product import Product
    from inventory import Inventory
    from vending_machine import VendingMachine

    inv = Inventory()
    snack = Product("Chips", 1.50, 1)
    inv.add_product(snack)
    vm = VendingMachine(inv)

    linked_btn = Button(vending_machine=vm)
    assert linked_btn.vending_machine == vm, "Button should reference the vending machine"

    # Confirm purchase through the button
    purchase_ok = linked_btn.confirmPurchase()
    assert purchase_ok is True, "Linked confirmPurchase should succeed for in-stock snack"
    assert snack.stock == 0, f"Expected stock 0, got {snack.stock}"
    print(f"[PASS] Linked button confirmed purchase: {snack.name} stock reduced to {snack.stock}")

    # Second purchase attempt through button should fail (sold out)
    purchase_fail = linked_btn.confirmPurchase()
    assert purchase_fail is False, "Linked confirmPurchase should fail when item sold out"
    print("[PASS] Linked button purchase correctly rejected when product sold out")

    print("--- All Button Assertions Passed Successfully! ---\n")
