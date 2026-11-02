"""
# main.py
# MobileMiniMart - Smart Vending Machine
# Main demonstration script tying together all 8 classes in a full simulation
# Team: M4O | Author: Mary Buoni
"""

from product import Product
from inventory import Inventory
from vending_machine import VendingMachine
from lcd import LCD
from knob import Knob
from led_strip import LEDStrip
from buzzer import Buzzer
from button import Button

def run_vending_machine_demo():
    """
    Demonstrates the complete MobileMiniMart workflow:
    1. Stocking the machine with snacks and drinks
    2. Powering on the display and status lights
    3. Browsing products using the knob
    4. Confirming a purchase using the button
    5. Handling a sold-out item with audio/visual error alerts
    """
    print("=" * 65)
    print("      WELCOME TO MOBILE MINI MART - SMART VENDING MACHINE")
    print("=" * 65)

    # ---------------------------------------------------------
    # Step 1: Initialize Hardware Components (Starter Stubs)
    # ---------------------------------------------------------
    print("\n[System] Initializing hardware components...")
    lcd = LCD()
    knob = Knob()
    led_strip = LEDStrip()
    buzzer = Buzzer()

    # ---------------------------------------------------------
    # Step 2: Initialize Products & Stock the Inventory
    # ---------------------------------------------------------
    print("\n[System] Stocking initial inventory...")
    chips = Product("Classic Chips", 1.50, 3)
    soda = Product("Sparkling Soda", 2.00, 1)
    candy = Product("Chocolate Bar", 1.25, 0)  # Sold out item
    pretzels = Product("Pretzels", 1.00, 4)

    inventory = Inventory()
    inventory.add_product(chips)
    inventory.add_product(soda)
    inventory.add_product(candy)
    inventory.add_product(pretzels)

    # ---------------------------------------------------------
    # Step 3: Initialize VendingMachine Controller & Button
    # ---------------------------------------------------------
    vm = VendingMachine(inventory)
    button = Button(vending_machine=vm)

    # Helper function to refresh outputs (LCD & LED Strip) based on current selection
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
    # Step 4: Machine Idle / Initial State
    # ---------------------------------------------------------
    print("\n--- 1. Machine Powered On & Ready ---")
    update_machine_outputs()

    # ---------------------------------------------------------
    # Step 5: Customer Turns Knob to Browse to Next Snack (Soda)
    # ---------------------------------------------------------
    print("\n--- 2. Customer Turns Knob (Browse to Soda) ---")
    knob.last_turn = 1  # Simulate turn
    vm.browseProducts()
    update_machine_outputs()

    # ---------------------------------------------------------
    # Step 6: Customer Presses Button to Buy Soda (Stock 1 -> 0)
    # ---------------------------------------------------------
    print("\n--- 3. Customer Presses Button to Confirm Purchase ---")
    button.pressed = True
    purchase_success = button.confirmPurchase()
    button.pressed = False

    if purchase_success:
        buzzer.playSuccess()
        print(">> Dispensing soda... Enjoy your drink!")
        update_machine_outputs()

    # ---------------------------------------------------------
    # Step 7: Customer Turns Knob to Candy (Stock 0 - Sold Out)
    # ---------------------------------------------------------
    print("\n--- 4. Customer Browses to Out-of-Stock Item (Candy) ---")
    knob.last_turn = 1
    vm.browseProducts()
    update_machine_outputs()

    # ---------------------------------------------------------
    # Step 8: Customer Tries to Buy Sold-Out Item
    # ---------------------------------------------------------
    print("\n--- 5. Customer Attempts to Buy Sold-Out Candy ---")
    button.pressed = True
    purchase_success = button.confirmPurchase()
    button.pressed = False

    if not purchase_success:
        buzzer.playError()
        print(">> Transaction rejected: Item is sold out!")

    # ---------------------------------------------------------
    # Step 9: Customer Browses Past End of List (Carousel Wrap)
    # ---------------------------------------------------------
    print("\n--- 6. Customer Scrolls Through Remaining Items (Carousel Wrap) ---")
    vm.browseProducts()  # Pretzels
    print(f"Viewing: {vm.selectProduct().name}")
    vm.browseProducts()  # Wraps back to Classic Chips
    print(f"Wrapped back to: {vm.selectProduct().name}")
    update_machine_outputs()

    print("\n" + "=" * 65)
    print("      MOBILE MINI MART DEMONSTRATION COMPLETE")
    print("=" * 65)


if __name__ == "__main__":
    run_vending_machine_demo()
