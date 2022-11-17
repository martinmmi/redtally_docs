from machine import Pin, I2C
from machine import Timer
from time import time
import ssd1306
import esp32


i2c = I2C(sda=Pin(21), scl=Pin(22), freq=100000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
devices = i2c.scan()                               # len(devices)           hex(device)

p25 = Pin(25, Pin.OUT)
p14 = Pin(14, Pin.OUT)

last_clk_state = 0             #Variablen fuer Takt
clk_state = 0
zStempel = int(time())

lastMillis1 = 0
lastMillis1 = int(time())

minutes = 0
timer = 0
temp_c = 0
hall = 0


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
    display.text("Temp: ", 0, 24, 1)
    display.text(converted_temp_c, 50, 24, 1)
    display.text("Hall: ", 0, 36, 1)
    display.text(converted_hall, 50, 36, 1)
    display.text("Time: ", 0, 48, 1)
    display.text(converted_minutes, 50, 48, 1)
    display.text("min", 80, 48, 1)
    display.show()
