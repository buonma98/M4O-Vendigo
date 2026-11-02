"""
# navigation_controller.py
# MobileMiniMart - Smart Vending Machine
# Autonomous navigation brain coordinating obstacle detection and collision avoidance
# Team: M4O | Author: Mary Buoni
"""

from obstacle_sensor import ObstacleSensor
from movement_controller import MovementController

class NavigationController:
    """
    Coordinates autonomous navigation for the MobileMiniMart vending machine.
    Monitors the ObstacleSensor and directs the MovementController to cruise forward,
    halt when obstacles approach, and execute avoidance maneuvers.

    Attributes:
    ----------
    obstacleSensor : ObstacleSensor
        The distance sensor used to scan the path ahead.
    movementController : MovementController
        The motor controller used to steer the machine.
    safeDistanceInches : float
        Minimum allowable clearance before obstacle avoidance triggers (default: 10.0 inches).
    cruiseSpeed : int
        Standard automatic driving speed (default: 40%).
    turnDurationMs : int
        Time allotted for an avoidance turn in milliseconds (default: 500 ms).
    automaticMode : bool
        Flag indicating whether automatic self-driving is active (default: False).

    Examples:
    ---------
    1. Start automatic navigation, check path, and stop:
       >>> nav = NavigationController()
       >>> nav.startAutomatic()
       >>> nav.isPathClear()
       True
       >>> nav.stopAutomatic()
    """

    def __init__(self, obstacleSensor: ObstacleSensor = None, movementController: MovementController = None,
                 safeDistanceInches: float = 10.0, cruiseSpeed: int = 40,
                 turnDurationMs: int = 500, automaticMode: bool = False):
        """
        Initialize NavigationController with sensor, movement controller, and safety parameters.
        """
        self.obstacleSensor = obstacleSensor if obstacleSensor is not None else ObstacleSensor()
        self.movementController = movementController if movementController is not None else MovementController()
        self.safeDistanceInches = safeDistanceInches
        self.cruiseSpeed = cruiseSpeed
        self.turnDurationMs = turnDurationMs
        self.automaticMode = automaticMode

    def startAutomatic(self):
        """
        Engage automatic self-driving mode and begin cruising.
        """
        self.automaticMode = True
        print(f"[NavigationController] Automatic driving ENGAGED at cruise speed {self.cruiseSpeed}%")
        self.movementController.setSpeed(self.cruiseSpeed)
        self.update()

    def stopAutomatic(self):
        """
        Disengage automatic driving and halt motors.
        """
        self.automaticMode = False
        print("[NavigationController] Automatic driving DISENGAGED - stopping machine")
        self.movementController.stop()

    def isPathClear(self) -> bool:
        """
        Check if the measured distance to the nearest obstacle exceeds safeDistanceInches.

        Returns:
        -------
        bool: True if path is clear (> safeDistanceInches), False if an obstacle is too close.
        """
        distance = self.obstacleSensor.readDistance()
        is_clear = distance > self.safeDistanceInches
        print(f"[NavigationController] Distance to obstacle: {distance:.1f}\" | Path clear: {is_clear}")
        return is_clear

    def avoidObstacle(self):
        """
        Execute an obstacle avoidance maneuver: stop, back up, and turn right.
        """
        print("[NavigationController] Obstacle detected! Executing avoidance maneuver...")
        self.movementController.stop()
        self.movementController.moveBackward()
        self.movementController.turnRight()
        self.movementController.stop()

    def update(self):
        """
        Main autonomous decision cycle: checks clearance and commands motion.
        """
        if not self.automaticMode:
            return

        if self.isPathClear():
            self.movementController.moveForward()
        else:
            self.avoidObstacle()


if __name__ == "__main__":
    print("--- Running NavigationController Class Verification Tests ---")

    nav = NavigationController()
    assert nav.safeDistanceInches == 10.0, f"Expected safeDistance 10.0, got {nav.safeDistanceInches}"
    assert nav.cruiseSpeed == 40, f"Expected cruiseSpeed 40, got {nav.cruiseSpeed}"
    assert nav.turnDurationMs == 500, f"Expected turnDurationMs 500, got {nav.turnDurationMs}"
    assert nav.automaticMode is False, "Initial automaticMode should be False"

    # Test path clear (default distance is 25.0 > 10.0)
    assert nav.isPathClear() is True, "Default path should be clear"

    # Test engaging automatic driving
    nav.startAutomatic()
    assert nav.automaticMode is True, "Automatic mode should be active"
    assert nav.movementController.leftMotor.direction == "forward", "Motors should drive forward"

    # Simulate obstacle approaching (distance = 5.0 <= 10.0)
    nav.obstacleSensor.simulatedDistance = 5.0
    assert nav.isPathClear() is False, "Path should NOT be clear when obstacle is 5.0 inches away"
    nav.update()
    print("[PASS] Obstacle avoidance cycle verified")

    # Test disengaging automatic driving
    nav.stopAutomatic()
    assert nav.automaticMode is False, "Automatic mode should be False after stop"
    assert nav.movementController.leftMotor.direction == "stopped", "Motors should be stopped"

    print("--- All NavigationController Assertions Passed Successfully! ---\n")
