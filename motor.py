"""
# motor.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing an individual DC motor driven via an H-Bridge
# Team: M4O | Author: Mary Buoni
"""

class Motor:
    """
    Represents an individual DC drive motor controlled via an H-Bridge motor driver.
    Supports bidirectional motion (forward, reverse, stop) with PWM speed regulation.

    Attributes:
    ----------
    forwardPin : object or None
        GPIO Pin hardware object for forward direction (default: None for simulation).
    reversePin : object or None
        GPIO Pin hardware object for reverse direction (default: None for simulation).
    enablePWM : object or None
        PWM hardware object for speed modulation (default: None for simulation).
    speed : int
        Current motor speed percentage from 0 (stopped) to 100 (full speed) (default: 0).
    direction : str
        Current motor status: "forward", "reverse", or "stopped" (default: "stopped").

    Examples:
    ---------
    1. Drive motor forward at speed 75, then stop:
       >>> motor = Motor()
       >>> motor.forward(75)
       >>> motor.stop()
    """

    def __init__(self, forwardPin=None, reversePin=None, enablePWM=None, speed: int = 0, direction: str = "stopped"):
        """
        Initialize the Motor with hardware pin mappings and default stopped state.
        """
        self.forwardPin = forwardPin
        self.reversePin = reversePin
        self.enablePWM = enablePWM
        self.speed = speed
        self.direction = direction

    def forward(self, speed: int):
        """
        Spin the motor in the forward direction at the specified speed.

        Parameters:
        ----------
        speed : int
            Speed percentage between 0 and 100.
        """
        self.speed = max(0, min(100, int(speed)))
        self.direction = "forward"
        print(f"[Motor] Driving FORWARD at speed {self.speed}%")

    def reverse(self, speed: int):
        """
        Spin the motor in the reverse direction at the specified speed.

        Parameters:
        ----------
        speed : int
            Speed percentage between 0 and 100.
        """
        self.speed = max(0, min(100, int(speed)))
        self.direction = "reverse"
        print(f"[Motor] Driving REVERSE at speed {self.speed}%")

    def stop(self):
        """
        Stop the motor and set speed to 0.
        """
        self.speed = 0
        self.direction = "stopped"
        print("[Motor] Motor STOPPED")

    def setSpeed(self, speed: int):
        """
        Update the current motor speed without altering direction.

        Parameters:
        ----------
        speed : int
            New speed percentage between 0 and 100.
        """
        self.speed = max(0, min(100, int(speed)))
        print(f"[Motor] Speed updated to {self.speed}% (direction: {self.direction})")


if __name__ == "__main__":
    print("--- Running Motor Class Verification Tests ---")

    motor = Motor()
    assert motor.speed == 0, f"Expected initial speed 0, got {motor.speed}"
    assert motor.direction == "stopped", f"Expected 'stopped', got {motor.direction}"

    # Test forward
    motor.forward(60)
    assert motor.speed == 60, f"Expected speed 60, got {motor.speed}"
    assert motor.direction == "forward", f"Expected 'forward', got {motor.direction}"

    # Test reverse
    motor.reverse(45)
    assert motor.speed == 45, f"Expected speed 45, got {motor.speed}"
    assert motor.direction == "reverse", f"Expected 'reverse', got {motor.direction}"

    # Test setSpeed
    motor.setSpeed(90)
    assert motor.speed == 90, f"Expected speed 90, got {motor.speed}"
    assert motor.direction == "reverse", "Direction should remain reverse"

    # Test stop
    motor.stop()
    assert motor.speed == 0, f"Expected speed 0, got {motor.speed}"
    assert motor.direction == "stopped", f"Expected 'stopped', got {motor.direction}"

    print("--- All Motor Assertions Passed Successfully! ---\n")
