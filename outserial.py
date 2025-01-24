import time
import board
import digitalio
import random
# Define pins
trigger = digitalio.DigitalInOut(board.GP15)  # Trigger pin
serial = digitalio.DigitalInOut(board.GP14)   # Serial data pin
clock = digitalio.DigitalInOut(board.GP17)    # Clock pin
ack = digitalio.DigitalInOut(board.GP18)      # ACK pin

# Set pin directions
trigger.direction = digitalio.Direction.OUTPUT
serial.direction = digitalio.Direction.OUTPUT
clock.direction = digitalio.Direction.OUTPUT
ack.direction = digitalio.Direction.INPUT

# Function to send binary data
def send_data(data):
    trigger.value = True  # Start transmission
    time.sleep(.001)
    for bit in data:
        
        #print(bit)
        serial.value = bool(int(bit))
        clock.value = True  # Clock HIGH
        time.sleep(0.001)   # Small delay for synchronization
        clock.value = False # Clock LOW
        time.sleep(0.001)   # Small delay for synchronization
        
    trigger.value = False  # End transmission

# Example data to send
voltage = random.randint(90,151)
current = random.randint(0,60)
temp = random.randint(15,32)

volt = f'{voltage:016b}'
cur =  f'{current:016b}'
temp = f'{temp:016b}'
data = volt + cur + temp

# Main loop
while True:
    voltage = random.randint(90,151)*100
    current = random.randint(0,60)*100
    temp = random.randint(15,32)*100
    print(voltage,current,temp)
    volt = f'{voltage:016b}'
    cur =  f'{current:016b}'
    temp = f'{temp:016b}'
    data = volt + cur + temp
    #print(data)
    send_data(data)
    #print('sent')
    time.sleep(.1)  # Wait 2 seconds before sending the next set of data

