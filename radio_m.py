import LCD_init
import os
import config
import sys
import time

from LCDscroll import *

LCD = LCD_init.lcd()

def radio(stacion_index):
    try:
        LCD.lcd_clear()
        global FM
        global FM_PLAY_INDEX
        global IP
        LCD.lcd_display_string("    RADIO FM", 1)
        LCD.lcd_display_string(config.FM_NAME[stacion_index][2], 2)
        time.sleep(3)
        song = os.popen('mocp -Q %song').read()
        song = song[:-1]
        LCD.lcd_clear()
        LCD.lcd_display_string(config.FM_NAME[stacion_index][2],1)
        if len(song) > 16:
            smooth_scroll(LCD, 16, song, 2, 0.8, 3)
        else:
            LCD.lcd_display_string(song, 2)
            time.sleep(10)
        LCD.lcd_clear()
        LCD.lcd_display_string("   "+time.strftime("%d-%m-%Y"),1)
        LCD.lcd_display_string("     "+time.strftime("%H:%M"),2)
        time.sleep(6.5)
    except:
        LCD.lcd_display_string("FM Error:\nFM load error")
        time.sleep(5)

os.system("mocp -l "+config.FM_NAME[int(sys.argv[1])][1])
while True:
    radio(int(sys.argv[1]))
