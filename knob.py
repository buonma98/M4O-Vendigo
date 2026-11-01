"""
# knob.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the rotary knob for browsing products
# Team: M4O | Author: Mary Buoni
"""

class Knob:
    """
    Represents the physical rotary knob (encoder/dial) on the vending machine.
    Used by customers to scroll/browse through the available snacks.

    NOTE: This is a starter class for our initial proposal.
    Physical hardware interfacing (GPIO rotary encoder pin monitoring)
    will be implemented in Phase 2. For now, it provides a software structure
    to simulate user turns.

    Parameters:
    ----------
    None

    Examples:
    ---------
    1. Read the knob turn status:
       >>> dial = Knob()
       >>> dial.readTurn()
       0
    """

    def __init__(self):
        """
        Initialize the Knob with a neutral position value.
        """
        # Tracks the simulated turn delta (1 for clockwise, -1 for counter-clockwise, 0 for none)
        self.last_turn = 0

    def readTurn(self) -> int:
        """
        Read whether the customer turned the knob.

        Returns:
        -------
        int: Direction of turn:
             1  = Turned clockwise (scroll to next product)
            -1  = Turned counter-clockwise (scroll to previous product)
             0  = No turn detected (idle)

        NOTE: This is a placeholder method. In Phase 2, this method will read
        signals from the Raspberry Pi Pico GPIO pins connected to the rotary encoder.
        """
        # Placeholder: Return the current simulated turn value
        return self.last_turn


if __name__ == "__main__":
    print("--- Running Knob Class Verification Tests ---")

    dial = Knob()
    assert dial.readTurn() == 0, "Initial turn reading should be 0 (idle)"

    # Test simulating clockwise turn
    dial.last_turn = 1
    assert dial.readTurn() == 1, "Simulated clockwise turn should return 1"

    # Test simulating counter-clockwise turn
    dial.last_turn = -1
    assert dial.readTurn() == -1, "Simulated counter-clockwise turn should return -1"

    # Test resetting to idle
    dial.last_turn = 0
    assert dial.readTurn() == 0, "Idle reset should return 0"

    print("--- All Knob Assertions Passed Successfully! ---\n")
