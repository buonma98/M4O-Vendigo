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

    Attributes:
    ----------
    pixels : object or None
        NeoPixel hardware driver instance (default: None for simulation).
    numLEDs : int
        Number of individual RGB LEDs on the strip (default: 8).
    brightness : float
        LED brightness scale from 0.0 to 1.0 (default: 0.5).
    readyColor : tuple[int, int, int]
        RGB color tuple for ready status (default: (0, 255, 0) Green).
    lowStockColor : tuple[int, int, int]
        RGB color tuple for low stock warning (default: (255, 180, 0) Yellow).
    outOfStockColor : tuple[int, int, int]
        RGB color tuple for out of stock status (default: (255, 0, 0) Red).

    Examples:
    ---------
    1. Change LED colors based on status:
       >>> leds = LEDStrip()
       >>> leds.showReady()
       >>> leds.showLowStock()
       >>> leds.showOutOfStock()
    """

    def __init__(self, pixels=None, numLEDs: int = 8, brightness: float = 0.5,
                 readyColor: tuple = (0, 255, 0),
                 lowStockColor: tuple = (255, 180, 0),
                 outOfStockColor: tuple = (255, 0, 0)):
        """
        Initialize the LED strip with hardware settings and color definitions.
        """
        self.pixels = pixels
        self.numLEDs = numLEDs
        self.brightness = brightness
        self.readyColor = readyColor
        self.lowStockColor = lowStockColor
        self.outOfStockColor = outOfStockColor

        # Tracks current color status ('READY', 'LOW_STOCK', 'OUT_OF_STOCK', or None)
        self.current_status = None

    def showReady(self):
        """
        Set the LED strip to GREEN (readyColor) to signal that the selected product is ready.
        """
        self.current_status = "READY"
        print(f"[LED Strip] Lights set to GREEN {self.readyColor} (Ready to purchase)")

    def showLowStock(self):
        """
        Set the LED strip to YELLOW (lowStockColor) to signal low inventory.
        """
        self.current_status = "LOW_STOCK"
        print(f"[LED Strip] Lights set to YELLOW {self.lowStockColor} (Warning: Low Stock)")

    def showOutOfStock(self):
        """
        Set the LED strip to RED (outOfStockColor) to signal sold-out status.
        """
        self.current_status = "OUT_OF_STOCK"
        print(f"[LED Strip] Lights set to RED {self.outOfStockColor} (Product Out of Stock)")


if __name__ == "__main__":
    print("--- Running LEDStrip Class Verification Tests ---")

    leds = LEDStrip()
    assert leds.numLEDs == 8, f"Expected 8 LEDs, got {leds.numLEDs}"
    assert leds.brightness == 0.5, f"Expected brightness 0.5, got {leds.brightness}"
    assert leds.readyColor == (0, 255, 0), "Expected green readyColor"
    assert leds.lowStockColor == (255, 180, 0), "Expected yellow lowStockColor"
    assert leds.outOfStockColor == (255, 0, 0), "Expected red outOfStockColor"
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
