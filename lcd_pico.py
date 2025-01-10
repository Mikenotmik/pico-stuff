import machine
import utime
import ujson

def save_data(count, counter):
    """Save count and counter values to a file."""
    with open("data.json", "w") as f:
        ujson.dump({"count": count, "counter": counter}, f)

def load_data():
    """Load count and counter values from a file."""
    try:
        with open("data.json", "r") as f:
            data = ujson.load(f)
            return data.get("count", 0), data.get("counter", 0)
    except (OSError, ValueError):
        # If the file doesn't exist or is corrupted, return default values
        return 0, 0

# Define pins
rs = machine.Pin(16, machine.Pin.OUT)
e = machine.Pin(17, machine.Pin.OUT)
d4 = machine.Pin(18, machine.Pin.OUT)
d5 = machine.Pin(19, machine.Pin.OUT)
d6 = machine.Pin(20, machine.Pin.OUT)
d7 = machine.Pin(21, machine.Pin.OUT)

def pulseE():
    e.value(0)
    utime.sleep_us(40)
    e.value(1)
    utime.sleep_us(40)

def send2LCD4(BinNum):
    d4.value((BinNum & 0b0001) >> 0)
    d5.value((BinNum & 0b0010) >> 1)
    d6.value((BinNum & 0b0100) >> 2)
    d7.value((BinNum & 0b1000) >> 3)
    pulseE()

def send2LCD8(BinNum):
    send2LCD4((BinNum & 0xF0) >> 4)  # Send high nibble
    send2LCD4(BinNum & 0x0F)         # Send low nibble

def setupLCD():
    rs.value(0)
    send2LCD4(0b0011)  # Initialize
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0010)  # 4-bit mode
    send2LCD8(0b00101000)  # Function set: 4-bit, 2-line
    send2LCD8(0b00001100)  # Display on, cursor off
    send2LCD8(0b00000110)  # Entry mode set
    send2LCD8(0b00000001)  # Clear display
    utime.sleep_ms(2)      # Wait for clear

def displayString(row, col, text):
    address = 0x80 + (0x40 * (row - 1)) + col
    rs.value(0)
    send2LCD8(address)  # Set DDRAM address
    rs.value(1)
    for char in text:
        send2LCD8(ord(char))

# Initialize LCD
setupLCD()

# Test display



