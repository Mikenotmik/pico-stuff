


from machine import Pin
import time
# Define the pins
trigger = Pin(15, Pin.IN, Pin.PULL_DOWN)  # Pin to detect the rising edge
serial  = Pin(14, Pin.IN, Pin.PULL_DOWN)     # Pin to read value from
clock   = Pin(17, Pin.IN, Pin.PULL_DOWN)
ack     = Pin(18, Pin.OUT)
led     = Pin(25, Pin.OUT) 

ack.value(0)
# Array to store binary bits
binary_array = []

# Callback function for rising edge detection
def on():
    binary_array = []
 
   
    while trigger.value():
        led.value(1)
        
        
        while not clock.value():
            if not trigger.value():
                if len(binary_array)>= 47:
                    print(binary_array[:16])
                    volt= int(''.join(str(bit) for bit in binary_array[:16]),2)
                    cur= int(''.join(str(bit) for bit in binary_array[16:32]),2)
                    temp= int(''.join(str(bit) for bit in binary_array[32:]),2)
                    print(volt/100,cur/100,temp/100)
                    #print(binary_array)
                    led.value(0)
               
                return binary_array
        
        binary_array.append(serial.value())
       
        
        while clock.value():
            pass
            



# Keep the program running
while True:
    
    if trigger.value():
        
        on()
      
        

