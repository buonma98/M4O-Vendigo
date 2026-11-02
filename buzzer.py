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
    - Success Tone: Cheerful high-frequency chime when a purchase is completed.
    - Error Tone: Low-frequency buzz when an action fails or a sold-out item is selected.

    Attributes:
    ----------
    pwm : object or None
        PWM hardware pin object for frequency synthesis on the Pico (default: None for simulation).
    successFrequency : int
        Audio frequency in Hz for success tones (default: 1000 Hz).
    errorFrequency : int
        Audio frequency in Hz for error tones (default: 250 Hz).
    durationMs : int
        Duration in milliseconds for audio beeps (default: 200 ms).

    Examples:
    ---------
    1. Play feedback sounds:
       >>> sound = Buzzer()
       >>> sound.playSuccess()
       >>> sound.playError()
    """

    def __init__(self, pwm=None, successFrequency: int = 1000, errorFrequency: int = 250, durationMs: int = 200):
        """
        Initialize the Buzzer with PWM audio frequencies and duration settings.
        """
        self.pwm = pwm
        self.successFrequency = successFrequency
        self.errorFrequency = errorFrequency
        self.durationMs = durationMs

        # Tracks the last sound played ('SUCCESS', 'ERROR', or None)
        self.last_sound = None

    def playSuccess(self):
        """
        Play a cheerful success chime at successFrequency (1000 Hz) for durationMs (200 ms).
        """
        self.last_sound = "SUCCESS"
        print(f"[Buzzer] Playing SUCCESS tone ({self.successFrequency}Hz for {self.durationMs}ms): *Ding-Ding!*")

    def playError(self):
        """
        Play an error buzz at errorFrequency (250 Hz) for durationMs (200 ms).
        """
        self.last_sound = "ERROR"
        print(f"[Buzzer] Playing ERROR tone ({self.errorFrequency}Hz for {self.durationMs}ms): *Buzzz!*")


if __name__ == "__main__":
    print("--- Running Buzzer Class Verification Tests ---")

    buzzer = Buzzer()
    assert buzzer.successFrequency == 1000, f"Expected 1000Hz, got {buzzer.successFrequency}"
    assert buzzer.errorFrequency == 250, f"Expected 250Hz, got {buzzer.errorFrequency}"
    assert buzzer.durationMs == 200, f"Expected 200ms, got {buzzer.durationMs}"
    assert buzzer.last_sound is None, "Initial sound state should be None"

    # Test playSuccess()
    buzzer.playSuccess()
    assert buzzer.last_sound == "SUCCESS", f"Expected 'SUCCESS', got '{buzzer.last_sound}'"

    # Test playError()
    buzzer.playError()
    assert buzzer.last_sound == "ERROR", f"Expected 'ERROR', got '{buzzer.last_sound}'"

    print("--- All Buzzer Assertions Passed Successfully! ---\n")
