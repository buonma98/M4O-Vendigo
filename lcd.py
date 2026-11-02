"""
# lcd.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the 16x2 character LCD display
# Team: M4O | Author: Mary Buoni
"""

class LCD:
    """
    Represents the 16x2 text LCD screen on the MobileMiniMart vending machine.
    Used to display product names, prices, stock counts, and status messages to the customer.

    Attributes:
    ----------
    i2c : object or None
        I2C bus object for Pico hardware communication (default: None for simulation).
    address : int
        I2C hex address of the LCD backpack (default: 0x27).
    rows : int
        Number of text rows on the LCD (default: 2).
    columns : int
        Number of characters per row (default: 16).

    Examples:
    ---------
    1. Display text on both lines and clear:
       >>> screen = LCD()
       >>> screen.displayLine1("Chips $1.50")
       >>> screen.displayLine2("Stock: 3")
       >>> screen.clear()
    """

    def __init__(self, i2c=None, address: int = 0x27, rows: int = 2, columns: int = 16):
        """
        Initialize the LCD screen with hardware configuration and empty display lines.
        """
        self.i2c = i2c
        self.address = address
        self.rows = rows
        self.columns = columns

        # Store the current text showing on Line 1 (up to 16 characters)
        self.line1 = ""

        # Store the current text showing on Line 2 (up to 16 characters)
        self.line2 = ""

    def displayLine1(self, text: str):
        """
        Display a text string on Line 1 of the LCD screen.

        Parameters:
        ----------
        text : str
            The message to display on the top line (e.g., 'Chips $1.50').
        """
        self.line1 = str(text)
        print(f"[LCD Line 1] {self.line1}")

    def displayLine2(self, text: str):
        """
        Display a text string on Line 2 of the LCD screen.

        Parameters:
        ----------
        text : str
            The message to display on the bottom line (e.g., 'Stock: 3').
        """
        self.line2 = str(text)
        print(f"[LCD Line 2] {self.line2}")

    def clear(self):
        """
        Clear all text from both lines of the LCD screen.
        """
        self.line1 = ""
        self.line2 = ""
        print("[LCD] Screen cleared")


if __name__ == "__main__":
    print("--- Running LCD Class Verification Tests ---")

    screen = LCD()
    assert screen.rows == 2, f"Expected 2 rows, got {screen.rows}"
    assert screen.columns == 16, f"Expected 16 columns, got {screen.columns}"
    assert screen.address == 0x27, f"Expected address 0x27, got {screen.address}"
    assert screen.line1 == "", "Initial Line 1 should be empty"
    assert screen.line2 == "", "Initial Line 2 should be empty"

    # Test displaying line 1
    screen.displayLine1("Chips $1.50")
    assert screen.line1 == "Chips $1.50", f"Expected 'Chips $1.50', got '{screen.line1}'"

    # Test displaying line 2
    screen.displayLine2("Stock: 3")
    assert screen.line2 == "Stock: 3", f"Expected 'Stock: 3', got '{screen.line2}'"

    # Test clearing screen
    screen.clear()
    assert screen.line1 == "", "Line 1 should be empty after clear()"
    assert screen.line2 == "", "Line 2 should be empty after clear()"

    print("--- All LCD Assertions Passed Successfully! ---\n")
