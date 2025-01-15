# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import digitalio
import adafruit_74hc595



spi = busio.SPI(board.GP2, MOSI=board.GP3)

latch_pin = digitalio.DigitalInOut(board.GP1)
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin)

# Create the pin objects in a list
pins = [sr.get_pin(n) for n in range(8)]

cs = board.GP15
cs = digitalio.DigitalInOut(cs)
cs.direction = digitalio.Direction.OUTPUT
cs.value = False

ack = board.GP16
ack = digitalio.DigitalInOut(ack)
ack.direction = digitalio.Direction.INPUT
ack.pull = digitalio.Pull.DOWN

data = 0
c= True
while True:
    if c == True:
        
        print('hey')
        
        for i,pin in enumerate(pins):
            pin.value =(data>>i)&1
        cs.value = True
        c=False
        
    
    if ack.value==True:
        
        
        cs.value =False
        for pin in pins:
            pin.value=False
        c=True
        data+=1
    time.sleep(.001)