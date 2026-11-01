"""
# led_strip.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the status LED light strip
# Team: M4O | Author: Mary Buoni
"""

class LEDStrip:
    """
    Represents the RGB NeoPixel LED strip on the MobileMiniMart vending machine.
    Provides visual color-coded feedback to the customer:
    - Green (Ready): Product is stocked and ready to purchase.
    - Yellow (Low Stock): Product inventory is running low (1 or 2 units).
    - Red (Out of Stock): Product is completely sold out.

    NOTE: This is a starter class for our initial proposal.
    Physical hardware interfacing (WS2812/NeoPixel signal generation on Pico GPIO)
    will be implemented in Phase 2. For now, it tracks and displays color status in software.

    Parameters:
    ----------
    None

    Examples:
    ---------
    1. Change LED colors based on status:
       >>> leds = LEDStrip()
       >>> leds.showReady()
       >>> leds.showLowStock()
       >>> leds.showOutOfStock()
    """

    def __init__(self):
        """
        Initialize the LED strip with no active color.
        """
        # Tracks current color status ('READY', 'LOW_STOCK', 'OUT_OF_STOCK', or None)
        self.current_status = None

    def showReady(self):
        """
        Set the LED strip to GREEN to signal that the selected product is ready for purchase.
        """
        self.current_status = "READY"
        # Placeholder: In Phase 2, this will send RGB (0, 255, 0) data to the NeoPixel strip
        print("[LED Strip] Lights set to GREEN (Ready to purchase)")

    def showLowStock(self):
        """
        Set the LED strip to YELLOW/AMBER to signal that the selected product is running low.
        """
        self.current_status = "LOW_STOCK"
        # Placeholder: In Phase 2, this will send RGB (255, 180, 0) data to the NeoPixel strip
        print("[LED Strip] Lights set to YELLOW (Warning: Low Stock)")

    def showOutOfStock(self):
        """
        Set the LED strip to RED to signal that the selected product is sold out.
        """
        self.current_status = "OUT_OF_STOCK"
        # Placeholder: In Phase 2, this will send RGB (255, 0, 0) data to the NeoPixel strip
        print("[LED Strip] Lights set to RED (Product Out of Stock)")


if __name__ == "__main__":
    print("--- Running LEDStrip Class Verification Tests ---")

    leds = LEDStrip()
    assert leds.current_status is None, "Initial LED status should be None"

    # Test Ready (Green)
    leds.showReady()
    assert leds.current_status == "READY", f"Expected 'READY', got '{leds.current_status}'"

    # Test Low Stock (Yellow)
    leds.showLowStock()
    assert leds.current_status == "LOW_STOCK", f"Expected 'LOW_STOCK', got '{leds.current_status}'"

    # Test Out of Stock (Red)
    leds.showOutOfStock()
    assert leds.current_status == "OUT_OF_STOCK", f"Expected 'OUT_OF_STOCK', got '{leds.current_status}'"

    print("--- All LEDStrip Assertions Passed Successfully! ---\n")
