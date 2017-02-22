# Raspberry Pi Radio

A simple radio with mp3 player support. Tested on Raspberry Pi 1 model B

#### Hardware requirements
  1. LCD with I2C converter
  2. 4x4 matrix keypad

#### Software requirements
  1. python3
  2. RPi.GPIO
  3. pad4pi (Requires a modification `GPIO.setmode(GPIO.BCM)` to `GPIO.setmode(GPIO.BOARD)`)
  4. alsaaudio
  5. python3-smbus
  6. netifaces
  
