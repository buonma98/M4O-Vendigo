"""
# main.py
# MobileMiniMart - Smart Vending Machine
# Main demonstration script tying together all 12 classes in a full simulation
# Team: M4O | Author: Mary Buoni
"""

from product import Product
from inventory import Inventory
from vending_machine import MobileVendingMachine
from lcd import LCD
from knob import Knob
from led_strip import LEDStrip
from buzzer import Buzzer
from button import Button
from motor import Motor
from movement_controller import MovementController
from obstacle_sensor import ObstacleSensor
from navigation_controller import NavigationController

def run_vending_machine_demo():
    """
    Demonstrates the complete MobileMiniMart workflow:
    1. Initializing all hardware components and mobility drivers
    2. Stocking the machine with snacks and beverages
    3. Autonomous driving and obstacle avoidance navigation
    4. Customer browsing using the analog knob
    5. Purchase confirmation using the physical push-button
    6. Audio and visual feedback (LCD display, LED status lights, Buzzer chime)
    7. Handling sold-out items with error alerts
    """
    print("=" * 70)
    print("      WELCOME TO MOBILE MINI MART - SMART AUTONOMOUS VENDING MACHINE")
    print("=" * 70)

    # ---------------------------------------------------------
    # Step 1: Initialize Mobility & Navigation (Motors & Sensor)
    # ---------------------------------------------------------
    print("\n[System] Initializing mobility and navigation controllers...")
    left_motor = Motor()
    right_motor = Motor()
    movement_controller = MovementController(leftMotor=left_motor, rightMotor=right_motor, defaultSpeed=50)
    obstacle_sensor = ObstacleSensor()
    navigation_controller = NavigationController(
        obstacleSensor=obstacle_sensor,
        movementController=movement_controller,
        safeDistanceInches=10.0,
        cruiseSpeed=40
    )

    # ---------------------------------------------------------
    # Step 2: Initialize Customer I/O Peripherals
    # ---------------------------------------------------------
    print("[System] Initializing customer interface peripherals...")
    lcd = LCD()
    knob = Knob()
    led_strip = LEDStrip()
    buzzer = Buzzer()

    # ---------------------------------------------------------
    # Step 3: Stock the Inventory
    # ---------------------------------------------------------
    print("[System] Stocking initial inventory...")
    chips = Product("Classic Chips", 1.50, 3)
    soda = Product("Sparkling Soda", 2.00, 1)
    candy = Product("Chocolate Bar", 1.25, 0)  # Sold out item
    pretzels = Product("Pretzels", 1.00, 4)

    inventory = Inventory(lowStockThreshold=2)
    inventory.addProduct(chips)
    inventory.addProduct(soda)
    inventory.addProduct(candy)
    inventory.addProduct(pretzels)

    # ---------------------------------------------------------
    # Step 4: Initialize MobileVendingMachine Master Controller
    # ---------------------------------------------------------
    vm = MobileVendingMachine(
        inventory=inventory,
        lcd=lcd,
        knob=knob,
        ledStrip=led_strip,
        buzzer=buzzer,
        movementController=movement_controller,
        navigationController=navigation_controller
    )
    button = Button(vending_machine=vm)
    vm.button = button

    # Helper function to refresh outputs (LCD & LED Strip)
    def update_machine_outputs():
        line1, line2 = vm.updateDisplay()
        lcd.displayLine1(line1)
        lcd.displayLine2(line2)

        status = vm.updateLEDStatus()
        if status == "Ready":
            led_strip.showReady()
        elif status == "Low Stock":
            led_strip.showLowStock()
        else:
            led_strip.showOutOfStock()

    # ---------------------------------------------------------
    # Step 5: Autonomous Driving to Customer Zone
    # ---------------------------------------------------------
    print("\n--- 1. Autonomous Navigation: Cruising to Snack Zone ---")
    vm.startAutomaticDriving()

    print("\n[Navigation] Sensor scans path ahead...")
    obstacle_sensor.simulatedDistance = 28.0  # Clear path (28 inches)
    navigation_controller.update()

    print("\n[Navigation] Customer approaches! Obstacle detected 8.0 inches away...")
    obstacle_sensor.simulatedDistance = 8.0  # Obstacle detected closer than 10.0" threshold
    navigation_controller.update()
    vm.stopAutomaticDriving()

    # ---------------------------------------------------------
    # Step 6: Machine Ready / Customer Interaction Starts
    # ---------------------------------------------------------
    print("\n--- 2. Machine Parked & Ready for Customer ---")
    update_machine_outputs()

    # ---------------------------------------------------------
    # Step 7: Customer Browses Using the Knob
    # ---------------------------------------------------------
    print("\n--- 3. Customer Turns Knob to Browse (Selects Sparkling Soda) ---")
    knob.currentValue = 32768  # Turn knob
    vm.browseProducts()
    print(f"[State] Machine awaitingConfirmation: {vm.awaitingConfirmation}")
    update_machine_outputs()

    # ---------------------------------------------------------
    # Step 8: Customer Confirms Purchase with Button
    # ---------------------------------------------------------
    print("\n--- 4. Customer Presses Button to Confirm Purchase ---")
    button.pressed = True
    purchase_ok = button.confirmPurchase()
    button.pressed = False

    if purchase_ok:
        buzzer.playSuccess()
        print(">> Dispensing soda... Enjoy your drink!")
        print(f"[State] Machine awaitingConfirmation reset to: {vm.awaitingConfirmation}")
        update_machine_outputs()

    # ---------------------------------------------------------
    # Step 9: Customer Browses to Out-of-Stock Item (Chocolate Bar)
    # ---------------------------------------------------------
    print("\n--- 5. Customer Browses to Out-of-Stock Item (Chocolate Bar) ---")
    knob.currentValue = 48000
    vm.browseProducts()
    update_machine_outputs()

    # ---------------------------------------------------------
    # Step 10: Attempting to Buy Sold-Out Item
    # ---------------------------------------------------------
    print("\n--- 6. Customer Attempts to Buy Sold-Out Item ---")
    button.pressed = True
    purchase_fail = button.confirmPurchase()
    button.pressed = False

    if not purchase_fail:
        buzzer.playError()
        print(">> Transaction rejected: Item is currently sold out!")

    # ---------------------------------------------------------
    # Step 11: Machine Resumes Cruising
    # ---------------------------------------------------------
    print("\n--- 7. Order Complete: Resuming Autonomous Route ---")
    obstacle_sensor.simulatedDistance = 30.0
    vm.startAutomaticDriving()
    vm.stopAutomaticDriving()

    print("\n" + "=" * 70)
    print("      MOBILE MINI MART FULL SYSTEM DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    run_vending_machine_demo()
