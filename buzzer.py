"""
# buzzer.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the audio feedback buzzer
# Team: M4O | Author: Mary Buoni
"""

class Buzzer:
    """
    Represents the piezo buzzer on the MobileMiniMart vending machine.
    Provides audible confirmation tones for user actions:
    - Success Tone: Cheerful chime when a purchase is completed.
    - Error Tone: Low buzz when an action fails or a sold-out item is selected.

    NOTE: This is a starter class for our initial proposal.
    Physical hardware interfacing (PWM frequency generation on Raspberry Pi Pico)
    will be implemented in Phase 2. For now, it logs tones and tracks sound state in software.

    Parameters:
    ----------
    None

    Examples:
    ---------
    1. Play feedback sounds:
       >>> sound = Buzzer()
       >>> sound.playSuccess()
       >>> sound.playError()
    """

    def __init__(self):
        """
        Initialize the Buzzer with an idle sound state.
        """
        # Tracks the last sound played ('SUCCESS', 'ERROR', or None)
        self.last_sound = None

    def playSuccess(self):
        """
        Play a cheerful success chime (two short high-pitched beeps).
        Triggered when a snack purchase is successfully confirmed.
        """
        self.last_sound = "SUCCESS"
        # Placeholder: In Phase 2, this will send PWM audio tones (e.g., 1000Hz then 1500Hz)
        print("[Buzzer] Playing SUCCESS tone: *Ding-Ding!* (Purchase complete)")

    def playError(self):
        """
        Play an error buzz (low-pitched buzz).
        Triggered when a customer tries to buy a sold-out snack or an error occurs.
        """
        self.last_sound = "ERROR"
        # Placeholder: In Phase 2, this will send PWM audio tone (e.g., 250Hz buzz)
        print("[Buzzer] Playing ERROR tone: *Buzzz!* (Action failed / Sold out)")


if __name__ == "__main__":
    print("--- Running Buzzer Class Verification Tests ---")

    buzzer = Buzzer()
    assert buzzer.last_sound is None, "Initial sound state should be None"

    # Test playSuccess()
    buzzer.playSuccess()
    assert buzzer.last_sound == "SUCCESS", f"Expected 'SUCCESS', got '{buzzer.last_sound}'"

    # Test playError()
    buzzer.playError()
    assert buzzer.last_sound == "ERROR", f"Expected 'ERROR', got '{buzzer.last_sound}'"

    print("--- All Buzzer Assertions Passed Successfully! ---\n")
