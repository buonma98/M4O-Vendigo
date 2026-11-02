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

    Attributes:
    ----------
    pin : object or None
        GPIO Pin hardware object on the Raspberry Pi Pico (default: None for simulation).
    lastPressed : bool
        The previous recorded state of the button (default: False).
    lastPressTime : int
        Timestamp of the last button event in milliseconds (default: 0).
    debounceMs : int
        Debounce window in milliseconds to prevent false double-clicks (default: 200 ms).

    Examples:
    ---------
    1. Check button state and confirm purchase:
       >>> btn = Button()
       >>> btn.isPressed()
       False
    """

    def __init__(self, pin=None, vending_machine=None, lastPressed: bool = False,
                 lastPressTime: int = 0, debounceMs: int = 200):
        """
        Initialize the Button with hardware pin, debounce settings, and machine reference.
        """
        self.pin = pin
        self.lastPressed = lastPressed
        self.lastPressTime = lastPressTime
        self.debounceMs = debounceMs

        # Reference to the VendingMachine controller
        self.vending_machine = vending_machine

        # Simulated press state for PC testing
        self.pressed = False

    def isPressed(self) -> bool:
        """
        Check if the button is currently pressed down.

        Returns:
        -------
        bool: True if pressed, False if unpressed/released.
        """
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

        if self.vending_machine is not None:
            return self.vending_machine.confirmPurchase()

        return True


if __name__ == "__main__":
    print("--- Running Button Class Verification Tests ---")

    btn = Button()
    assert btn.debounceMs == 200, f"Expected debounceMs 200, got {btn.debounceMs}"
    assert btn.lastPressed is False, "Initial lastPressed should be False"
    assert btn.lastPressTime == 0, "Initial lastPressTime should be 0"
    assert btn.isPressed() is False, "Initial button state should be unpressed (False)"

    # Test simulated press
    btn.pressed = True
    assert btn.isPressed() is True, "Button should report pressed (True)"

    btn.pressed = False
    assert btn.isPressed() is False, "Button should report unpressed (False)"

    # Standalone confirmPurchase call
    result = btn.confirmPurchase()
    assert result is True, "Standalone confirmPurchase() should return True"
    print("[PASS] Standalone button state and debounce settings verified")

    print("--- All Button Assertions Passed Successfully! ---\n")
