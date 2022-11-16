from machine import Pin, I2C
import ssd1306
import esp32
import time

i2c = I2C(sda=Pin(21), scl=Pin(22), freq=100000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
devices = i2c.scan()                               # len(devices)           hex(device)

while(True):

    time.sleep_ms(500)
    temp = esp32.raw_temperature()                            # read the internal temperature of the MCU, in Fahrenheit
    temp_c = ((temp - 32) * 5/9)
    converted_temp_c = str(temp_c)

    hall = esp32.hall_sensor()
    converted_hall = str(hall)



    display.fill(0)
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.vline(9, 8, 22, 1)
    display.vline(16, 2, 22, 1)
    display.vline(23, 8, 22, 1)
    display.fill_rect(26, 24, 2, 4, 1)
    display.text('TEST', 40, 0, 1)
    display.text('SSD1306', 40, 12, 1)
    display.text('OLED 128x64', 40, 24, 1)
    display.text(converted_temp_c, 40, 36, 1)
    display.text(converted_hall, 40, 48, 1)
    display.show()
