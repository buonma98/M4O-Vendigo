"""
# movement_controller.py
# MobileMiniMart - Smart Vending Machine
# Dual-motor differential drive controller for mobility and steering
# Team: M4O | Author: Mary Buoni
"""

from motor import Motor

class MovementController:
    """
    Controls the differential drive mobility system for MobileMiniMart.
    Orchestrates two motors (leftMotor and rightMotor) to move forward,
    move backward, turn left, turn right, and stop.

    Attributes:
    ----------
    leftMotor : Motor
        The Motor instance driving the left wheel.
    rightMotor : Motor
        The Motor instance driving the right wheel.
    defaultSpeed : int
        Standard cruising speed percentage from 0 to 100 (default: 50).

    Examples:
    ---------
    1. Drive forward, steer right, and stop:
       >>> mc = MovementController()
       >>> mc.moveForward()
       >>> mc.turnRight()
       >>> mc.stop()
    """

    def __init__(self, leftMotor: Motor = None, rightMotor: Motor = None, defaultSpeed: int = 50):
        """
        Initialize the MovementController with left and right motors and default speed.
        """
        self.leftMotor = leftMotor if leftMotor is not None else Motor()
        self.rightMotor = rightMotor if rightMotor is not None else Motor()
        self.defaultSpeed = defaultSpeed

    def moveForward(self):
        """
        Drive both motors forward at defaultSpeed to propel the machine forward.
        """
        print(f"[MovementController] Moving FORWARD at speed {self.defaultSpeed}%")
        self.leftMotor.forward(self.defaultSpeed)
        self.rightMotor.forward(self.defaultSpeed)

    def moveBackward(self):
        """
        Drive both motors in reverse at defaultSpeed to back up.
        """
        print(f"[MovementController] Moving BACKWARD at speed {self.defaultSpeed}%")
        self.leftMotor.reverse(self.defaultSpeed)
        self.rightMotor.reverse(self.defaultSpeed)

    def turnLeft(self):
        """
        Execute a pivot turn to the left by reversing left motor and driving right motor forward.
        """
        print(f"[MovementController] Turning LEFT at speed {self.defaultSpeed}%")
        self.leftMotor.reverse(self.defaultSpeed)
        self.rightMotor.forward(self.defaultSpeed)

    def turnRight(self):
        """
        Execute a pivot turn to the right by driving left motor forward and reversing right motor.
        """
        print(f"[MovementController] Turning RIGHT at speed {self.defaultSpeed}%")
        self.leftMotor.forward(self.defaultSpeed)
        self.rightMotor.reverse(self.defaultSpeed)

    def stop(self):
        """
        Halt both motors immediately.
        """
        print("[MovementController] STOPPING all motors")
        self.leftMotor.stop()
        self.rightMotor.stop()

    def setSpeed(self, speed: int):
        """
        Adjust the default cruising speed.

        Parameters:
        ----------
        speed : int
            New speed percentage between 0 and 100.
        """
        self.defaultSpeed = max(0, min(100, int(speed)))
        print(f"[MovementController] Default speed set to {self.defaultSpeed}%")


if __name__ == "__main__":
    print("--- Running MovementController Class Verification Tests ---")

    mc = MovementController()
    assert mc.defaultSpeed == 50, f"Expected defaultSpeed 50, got {mc.defaultSpeed}"
    assert mc.leftMotor.speed == 0, "Left motor should be stopped"
    assert mc.rightMotor.speed == 0, "Right motor should be stopped"

    # Test moveForward
    mc.moveForward()
    assert mc.leftMotor.direction == "forward", "Left motor should be forward"
    assert mc.rightMotor.direction == "forward", "Right motor should be forward"
    assert mc.leftMotor.speed == 50
    assert mc.rightMotor.speed == 50

    # Test turnLeft
    mc.turnLeft()
    assert mc.leftMotor.direction == "reverse", "Left motor should reverse for left turn"
    assert mc.rightMotor.direction == "forward", "Right motor should forward for left turn"

    # Test turnRight
    mc.turnRight()
    assert mc.leftMotor.direction == "forward", "Left motor should forward for right turn"
    assert mc.rightMotor.direction == "reverse", "Right motor should reverse for right turn"

    # Test moveBackward
    mc.moveBackward()
    assert mc.leftMotor.direction == "reverse"
    assert mc.rightMotor.direction == "reverse"

    # Test stop
    mc.stop()
    assert mc.leftMotor.direction == "stopped"
    assert mc.rightMotor.direction == "stopped"

    # Test setSpeed
    mc.setSpeed(75)
    assert mc.defaultSpeed == 75, f"Expected 75, got {mc.defaultSpeed}"

    print("--- All MovementController Assertions Passed Successfully! ---\n")
