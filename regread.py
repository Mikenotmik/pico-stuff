import board , time
import digitalio


pins = [board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21]


pins = [digitalio.DigitalInOut(pin) for pin in pins]


for pin in pins:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.DOWN  
#input ready
cs = board.GP22
cs = digitalio.DigitalInOut(cs)
cs.direction = digitalio.Direction.INPUT
cs.pull = digitalio.Pull.DOWN

#input acknowledge

ack = board.GP12
ack = digitalio.DigitalInOut(ack)
ack.direction = digitalio.Direction.OUTPUT
ack.value = False

#led to confirm
led = board.LED
led = digitalio.DigitalInOut(led)
led.direction = digitalio.Direction.OUTPUT
led.value=False
ipkus =[]
key= False
while True:
    ipkus = []
    
    if cs.value and not key:
        led.value=True
        for huh in pins:
            ipkus.append(huh.value &1)
        value =''.join(str(bit) for bit in reversed(ipkus))
        value= int(value,2)
        print(ipkus,value)
        ack.value = True
        time.sleep(.005)
        ack.value = False
        
    
        
    if not cs:
        print(cs.value)
        led.value=False
        key = False
    

