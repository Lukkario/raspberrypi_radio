#!/usr/bin/python

import os
import LCD_init
import time
from LCDscroll import *

LCD = LCD_init.lcd()
LCD.lcd_clear()
LCD.lcd_display_string("   MP3 PLAYER", 1)

def getSongName():
        wait_time = 0
        song = os.popen('mocp -Q %song').read()
        song = song[:-1]
        song_len = os.popen('mocp -Q %tl').read()
        if song != '' or song_len != '':
            while song == '':
                song = os.popen('mocp -Q %song').read()
                song = song[:-1]
            while song_len == '':
                song_len = os.popen('mocp -Q %tl').read()
            song_len = song_len.split(':')
            time.sleep(0.2)
            if len(song) > 16:
                smooth_scroll(LCD, 16, song, 2, 0.6)
            else:
                wait_time = int(song_len[0]) * 60 + int(song_len[1])
                LCD.lcd_display_string(" "*16,2)
                LCD.lcd_display_string(song,2)
                sleep(wait_time)

        else:
            LCD.lcd_display_string("Wysapil blad", 2)
            return False

while True:
    getSongName()
