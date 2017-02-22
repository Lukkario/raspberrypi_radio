from time import sleep, strftime
import LCD_init

LCD = LCD_init.lcd()
LCD.lcd_clear()
LCD.lcd_display_string("   "+strftime("%d-%m-%Y"),1)
LCD.lcd_display_string("     "+strftime("%H:%M"),2)
curtime = strftime("%H:%M")

while True:
    if curtime != strftime("%H:%M"):
        LCD.lcd_clear()
        LCD.lcd_display_string("   "+strftime("%d-%m-%Y"),1)
        LCD.lcd_display_string("     "+strftime("%H:%M"),2)
        curtime = strftime("%H:%M")
    sleep(5)
