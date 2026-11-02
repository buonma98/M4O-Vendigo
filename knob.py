"""
# knob.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the analog potentiometer knob for browsing products
# Team: M4O | Author: Mary Buoni
"""

class Knob:
    """
    Represents the physical potentiometer knob on the vending machine.
    Connected to an Analog-to-Digital Converter (ADC) pin on the Pico.
    Used by customers to scroll/browse through the available snacks.

    Attributes:
    ----------
    adc : object or None
        ADC hardware object on the Raspberry Pi Pico (default: None for simulation).
    minValue : int
        Minimum raw ADC reading (default: 0).
    maxValue : int
        Maximum raw ADC reading (default: 65535 for Pico 16-bit ADC).

    Examples:
    ---------
    1. Read the knob ADC value:
       >>> dial = Knob()
       >>> dial.readValue()
       0
    """

    def __init__(self, adc=None, minValue: int = 0, maxValue: int = 65535):
        """
        Initialize the Knob with ADC hardware and range constraints.
        """
        self.adc = adc
        self.minValue = minValue
        self.maxValue = maxValue

        # Simulated ADC reading for testing on PC
        self.currentValue = minValue

    def readValue(self) -> int:
        """
        Read the current raw ADC integer value from the potentiometer knob.

        Returns:
        -------
        int: Value between minValue (0) and maxValue (65535).
        """
        return self.currentValue

    def readTurn(self) -> int:
        """
        Helper method returning simulated turn direction:
        1 for forward, -1 for backward, 0 for idle.
        """
        # Return 1 if turned clockwise, -1 if counter-clockwise, 0 if neutral
        if self.currentValue > self.minValue:
            return 1
        return 0


if __name__ == "__main__":
    print("--- Running Knob Class Verification Tests ---")

    dial = Knob()
    assert dial.minValue == 0, f"Expected minValue 0, got {dial.minValue}"
    assert dial.maxValue == 65535, f"Expected maxValue 65535, got {dial.maxValue}"
    assert dial.readValue() == 0, "Initial reading should be 0"

    # Test reading simulated position
    dial.currentValue = 32768  # Halfway turn
    assert dial.readValue() == 32768, f"Expected 32768, got {dial.readValue()}"
    print(f"[PASS] Analog Knob readValue() returned: {dial.readValue()}")

    # Test full turn
    dial.currentValue = 65535
    assert dial.readValue() == 65535, f"Expected 65535, got {dial.readValue()}"
    print(f"[PASS] Analog Knob at max reading: {dial.readValue()}")

    print("--- All Knob Assertions Passed Successfully! ---\n")
