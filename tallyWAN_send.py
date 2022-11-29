import gc
from esp32 import *
import neopixel
import ssd1306


import machine
from machine import Pin, SPI
from time import time
from lora_lib import LoRa
from ssd1306_lib import SSD1306_I2C

# I2C pins
i2c = machine.I2C(sda=machine.Pin(21), scl=machine.Pin(22))
i2c.scan()
display = SSD1306_I2C(128, 64, i2c)

# Output-Input pins
p25 = Pin(25, Pin.OUT)
p14 = Pin(14, Pin.OUT)
p35 = Pin(35, Pin.IN)

# SPI pins
SCK  = 5
MOSI = 27
MISO = 19

# Chip select
CS   = 18

# Receive IRQ
RX   = 26

# Setup some Variables
last_clk_state = 0
clk_state = 0
zStempel = int(time())
lastMillis1 = 0
lastMillis1 = int(time())
minutes = 0
timer = 0
temp_c = 0
hall = 0
message = 0

# Setup SPI
spi = SPI(
    1,
    baudrate=10000000,
    sck=Pin(SCK, Pin.OUT, Pin.PULL_DOWN),
    mosi=Pin(MOSI, Pin.OUT, Pin.PULL_UP),
    miso=Pin(MISO, Pin.IN, Pin.PULL_UP),
)
spi.init()

# Setup LoRa
lora = LoRa(
    spi,
    cs=Pin(CS, Pin.OUT),
    rx=Pin(RX, Pin.IN),
    frequency=868.0,
    bandwidth=250000,
    spreading_factor=10,
    coding_rate=5,
)

while True:

    #CLOCK
    if clk_state == 0 and int(time()) - zStempel < 1:
        clk_state = 1

    if clk_state == 1 and int(time()) - zStempel >= 1:
        if int(time()) - zStempel <= 2:
            clk_state = 0

    if last_clk_state != clk_state:
        last_clk_state = clk_state
        p14.value(clk_state)
        p25.value(clk_state)

        if clk_state == 1:
            message += 1
            converted_message = str(message)
            lora.send(converted_message)
            print("SEND: ")
            print(converted_message)

    if int(time()) - zStempel >= 2:
        zStempel = int(time())

    #MILLIS CLOCK
    if int(time()) - lastMillis1 >= 1:
        temp = esp32.raw_temperature()  # read the internal temperature of the MCU, in Fahrenheit
        temp_c = ((temp - 32) * 5 / 9)

        hall = esp32.hall_sensor()

        lastMillis1 = int(time())

    converted_temp_c = str(temp_c)
    converted_hall = str(hall)
    converted_clk_state = str(clk_state)

    minutes = int(time()/60)
    converted_minutes = str(minutes)

    display.contrast(255)
    display.invert(0)
    display.fill(0)
    display.text('TallyWAN', 0, 0, 1)
    display.text("CLK", 88, 0, 1)
    display.text(converted_clk_state, 115, 0, 1)
    display.text("SEND:", 0, 24, 1)
    display.text(converted_message, 50, 24, 1)
    display.text("Temp: ", 0, 36, 1)
    display.text(converted_temp_c, 50, 36, 1)
    display.text("Time: ", 0, 48, 1)
    display.text(converted_minutes, 50, 48, 1)
    display.text("min", 80, 48, 1)
    display.show()
