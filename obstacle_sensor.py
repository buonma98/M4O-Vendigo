"""
# obstacle_sensor.py
# MobileMiniMart - Smart Vending Machine
# Starter class representing the HC-SR04 ultrasonic distance sensor
# Team: M4O | Author: Mary Buoni
"""

class ObstacleSensor:
    """
    Represents the ultrasonic obstacle detection sensor on MobileMiniMart.
    Uses echolocation (trigger and echo ultrasonic sound waves) to measure
    the distance to upcoming walls, tables, and customers in real-time.

    Attributes:
    ----------
    triggerPin : object or None
        GPIO Pin hardware object that transmits the ultrasonic burst (default: None).
    echoPin : object or None
        GPIO Pin hardware object that measures echo pulse return time (default: None).
    timeoutUs : int
        Maximum pulse wait timeout in microseconds (default: 30000 us).

    Examples:
    ---------
    1. Read distance from obstacle sensor:
       >>> sensor = ObstacleSensor()
       >>> sensor.readDistance()
       25.0
    """

    def __init__(self, triggerPin=None, echoPin=None, timeoutUs: int = 30000):
        """
        Initialize the ObstacleSensor with hardware pin assignments and timeout.
        """
        self.triggerPin = triggerPin
        self.echoPin = echoPin
        self.timeoutUs = timeoutUs

        # Simulated distance in inches for PC testing (default: 25.0 inches - clear path)
        self.simulatedDistance = 25.0

    def readDistance(self) -> float:
        """
        Measure and return the distance to the nearest obstacle in inches.

        Returns:
        -------
        float: Distance measurement in inches.
        """
        # Placeholder: In Phase 2, this will calculate (pulse_time * 0.0343 / 2) / 2.54 on Pico
        return float(self.simulatedDistance)


if __name__ == "__main__":
    print("--- Running ObstacleSensor Class Verification Tests ---")

    sensor = ObstacleSensor()
    assert sensor.timeoutUs == 30000, f"Expected timeoutUs 30000, got {sensor.timeoutUs}"
    assert sensor.readDistance() == 25.0, f"Expected default distance 25.0, got {sensor.readDistance()}"

    # Test reading close obstacle
    sensor.simulatedDistance = 6.5
    assert sensor.readDistance() == 6.5, f"Expected 6.5 inches, got {sensor.readDistance()}"
    print(f"[PASS] ObstacleSensor readDistance() returned: {sensor.readDistance():.1f} inches")

    print("--- All ObstacleSensor Assertions Passed Successfully! ---\n")
