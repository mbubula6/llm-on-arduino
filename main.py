from machine import I2C, Pin
from DIYables_MicroPython_LCD_I2C import LCD_I2C
import utime

I2C_ADDR = 0x27 #I2C address of LCD (not sure yet)

LCD_ROWS = 2
LCD_COLUMNS = 16

i2c = I2C(1) #initializing I2C

lcd = LCD_I2C(i2c, I2C_ADDR, LCD_ROWS, LCD_COLUMNS)

# Setup again
lcd.backlight_on()
lcd.clear()

# main loop (program)
while True:
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.print("Hi!!!")
    lcd.set_cursor(0, 1)
    lcd.print("There will be an AI")
    utime.sleep(4)
