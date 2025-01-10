from machine import Pin
import time
import utime
import ujson
from lcd_pico import *

# Pins setup
relay = Pin(15, Pin.OUT)
relay1 = Pin(14, Pin.OUT)

# Load saved values
count, counter = load_data()

# Setup LCD
setupLCD()
displayString(1, 0, "how many")
displayString(2, 0, "how much")

start = time.time()

while True:
    time.sleep(0.25)
    relay1.toggle()
    count += 1
    displayString(2, 9, f"{count}")
    
    if abs(time.time() - start) >= 0.5:
        count += 1
        counter += 1
        relay1.toggle()
        relay.toggle()
        start = time.time()
        displayString(1, 9, f"{counter}")
        
        # Save the current state periodically
        save_data(count, counter)

    '''if count / 2 >= 10_000:
        break'''

