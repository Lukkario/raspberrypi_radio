import LCD_init
import RPi.GPIO as GPIO
from LCDscroll import *

LCD = LCD_init.lcd()
LCD.lcd_clear()

def test_lcd():
    print("     [+] TESTING TEXT DISPLAY")
    LCD.lcd_display_string("0123456789ABCDEF", 1)
    LCD.lcd_display_string("0123456789ABCDEF", 2)
    sleep(5)
    #LCD.lcd_clear()
    print("     [+] TESTING LCD BACKLIGHT")
    LCD.backlight(0)
    sleep(5)
    LCD.backlight(1)
    sleep(3)
    print("     [+] LCD TEST DONE")

def test_lcd_scroll():
    for i in range(1,3):
        print("     [+] TESTING SCROLLING ON LINE "+str(i))
        scroll(LCD, 16, "This is a very long text just for test the scrolling function on line "+str(i), i, 1)
        LCD.lcd_clear()

def test_lcd_smooth_scroll():
    for i in range(1,3):
        print("     [+] TESTING SCROLLING ON LINE "+str(i))
        text = "This is a very very long text for testing scroll function"
        smooth_scroll(LCD, 16, text, i, 0.6, 1)
        LCD.lcd_clear()


def test_keypad():
    MATRIX = [ [1,2,3,'A'],
               [4,5,6,'B'],
               [7,8,9,'C'],
               ['*',0,'#','D'] ]
    ROW = [7,8,10,12]
    COL = [13,15,16,18]

    keypad_layout = """
                        +---+---+---+---+
                        | 1 | 2 | 3 | A |
                        +---+---+---+---+
                        | 4 | 5 | 6 | B |
                        +---+---+---+---+
                        | 7 | 8 | 9 | C |
                        +---+---+---+---+
                        | * | 0 | # | D |
                        +---+---+---+---+
               Keyboard interrupt to stop testing
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #GPIO.cleanup()
    for j in range(4):
        GPIO.setup(COL[j], GPIO.OUT)
        GPIO.output(COL[j], 1)

    for i in range(4):
        GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    print(keypad_layout)

    try:
        while True:
            for j in range(4):
                GPIO.output(COL[j],0)
                for i in range(4):
                    if GPIO.input(ROW[i]) == 0:
                        if MATRIX[i][j] == 1:
                            print("Pressed button: 1")
                        if MATRIX[i][j] == 2:
                            print("Pressed button: 2")
                        if MATRIX[i][j] == 3:
                            print("Pressed button: 3")
                        if MATRIX[i][j] == 4:
                            print("Pressed button: 4")
                        if MATRIX[i][j] == 5:
                            print("Pressed button: 5")
                        if MATRIX[i][j] == 6:
                            print("Pressed button: 6")
                        if MATRIX[i][j] == 7:
                            print("Pressed button: 7")
                        if MATRIX[i][j] == 8:
                            print("Pressed button: 8")
                        if MATRIX[i][j] == 9:
                            print("Pressed button: 9")
                        if MATRIX[i][j] == 0:
                            print("Pressed button: 0")
                        if MATRIX[i][j] == "*":
                            print("Pressed button: *")
                        if MATRIX[i][j] == "#":
                            print("Pressed button: #")
                        if MATRIX[i][j] == "A":
                            print("Pressed button: A")
                        if MATRIX[i][j] == "B":
                            print("Pressed button: B")
                        if MATRIX[i][j] == "C":
                            print("Pressed button: C")
                        if MATRIX[i][j] == "D":
                            print("Pressed button: D")
                        sleep(0.2)
                        while(GPIO.input(ROW[i]) == 0):
                                try:
                                    pass
                                except:
                                    return false
                GPIO.output(COL[j],1)
            sleep(0.1)
    except KeyboardInterrupt:
        print("     [+] Exiting keypad testing sequence...")


def main():
    print("[+] STARTING TESTING")
    print("[+] LCD TEST")
    test_lcd()
    print("[+] LCD SCROLL TEST")
    test_lcd_scroll()
    print("[+] LCD SMOOTH SCROLL TEST")
    test_lcd_smooth_scroll()
    print("[+] KEYPAD TEST")
    test_keypad()
    print("[+] EXITING TESTING")

if __name__ == "__main__":
    main()
