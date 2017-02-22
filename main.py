#!/usr/bin/python3

#import
import RPi.GPIO as GPIO
import os
import time
import LCD_init
import alsaaudio
from config import MUSIC_DIR, IFACE, SOUND_CARD
from subprocess import call
from iface_m import getInterfaceAddress
from time import gmtime, strftime
from pad4pi import rpi_gpio

#init lcd
LCD = LCD_init.lcd()

#set keyboard matrix
MATRIX = [ [1,2,3,'A'],
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D'] ]
ROW = [7,8,10,12]
COL = [13,15,16,18]

#init alsa mixer
mixer = alsaaudio.Mixer(SOUND_CARD)

#setup mocp and global vars
os.system("mocp -S")
FM = False
FM_PLAY_INDEX = ""
IP = False
MP3 = False

def Welcome():
    os.system("python3 welcome_m.py&")

def radio_start(index):
    global FM, MP3, FM_PLAY_INDEX, IP
    FM_PLAY_INDEX = index
    os.system("pkill python")
    os.system("python3 radio_m.py "+str(FM_PLAY_INDEX)+" &")
    FM = True
    IP = False
    MP3 = False

def mp3_start():
    global FM, MP3, FM_PLAY_INDEX, IP
    os.system("pkill python")
    os.system("mocp -l "+MUSIC_DIR+"/*")
    time.sleep(0.2)
    os.system("python3 mp3_m.py&")
    FM = False
    MP3 = True
    IP = False

def mp3_play():
    global FM, MP3
    try:
        os.system("mocp -U")
        os.system("pkill python")
        if FM == True:
            os.system("python3 radio_m.py "+str(FM_PLAY_INDEX)+" &")
        elif MP3 == True:
            time.sleep(1)
            os.system("python3 mp3_m.py&")
    except:
        pass

def mp3_change(direction):
    global FM, IP
    if FM == False:
        IP = False
        os.system("pkill python")
        os.system("mocp --"+direction)
        time.sleep(0.2)
        os.system("python3 mp3_m.py&")

def show_ip():
    global IP, FM, MP3
    try:
        os.system("pkill python")
        if IP == False:
            LCD.lcd_clear()
            eth = getInterfaceAddress(IFACE[0])
            wlan = getInterfaceAddress(IFACE[1])
            LCD.lcd_display_string("E:"+eth,1)
            LCD.lcd_display_string("W:"+wlan,2)
            IP = True
        else:
            if FM == True:
                IP = False
                os.system("python3 radio_m.py "+str(FM_PLAY_INDEX)+" &")
            elif MP3 == True:
                time.sleep(1)
                os.system("python3 mp3_m.py&")
    except:
        pass

def key_pause():
    os.system("mocp -P")
    os.system("pkill python")
    LCD.lcd_clear()
    LCD.lcd_display_string("     Pauza", 2)

def key_vol_up():
    vol = mixer.getvolume()
    if vol[0] != 100:
        mixer.setvolume(vol[0]+5)

def key_vol_down():
    vol = mixer.getvolume()
    if vol[0] != 0:
          mixer.setvolume(vol[0]-5)

def key_exit():
    global go
    os.system("mocp -x")
    go = 0
    try:
        return False
    except:
        return False

def key_action(key):
    if key == 1:
        radio_start(0)
    if key == 2:
        radio_start(1)
    if key == 3:
        radio_start(2)
    if key == 4:
        radio_start(3)
    if key == 5:
        radio_start(4)
    if key == 6:
        radio_start(5)
    if key == 7:
        radio_start(6)
    if key == 8:
        show_ip()
    if key == 9:
        mp3_start()
    if key == "*":
        key_pause()
    if key == "#":
        mp3_play()
    if key == "A":
        key_vol_up()
    if key == "B":
        key_vol_down()
    if key == "C":
        mp3_change("next")
    if key == "D":
        mp3_change("previous")
    if key == 0:
        key_exit()


def main():
  global FM, MP3, FM_PLAY_INDEX, IP, go
  Welcome()
  try:
      go = 1
      #Init matrix keypad
      factory = rpi_gpio.KeypadFactory()
      keypad = factory.create_keypad(keypad=MATRIX, row_pins=ROW, col_pins=COL)
      keypad.registerKeyPressHandler(key_action)
      while go:
          time.sleep(0.5)
  except KeyboardInterrupt:
      pass
  finally:
      keypad.cleanup()

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    os.system("pkill python")
    os.system("mocp -x")
    LCD.lcd_clear()
    LCD.lcd_display_string(" Do uslyszenia",1)
    LCD.lcd_display_string("       :)",2)
    time.sleep(2)
    LCD.lcd_clear()
    LCD.backlight(0)
    #os.system("sudo poweroff")
