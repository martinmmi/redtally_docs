from machine import Pin, I2C
import ssd1306

import time

i2c = I2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

i = 0
print('Hello TallyWAN')

while True:
    i = i + 1
    print(i)
    display.text(1, 0, 20, 1)
    display.show()
    time.sleep(0.5)
    display.fill(0)
    display.show()
    time.sleep(0.5)