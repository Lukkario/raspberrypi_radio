from time import sleep

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

def scroll(LCD, width, text, line, pause_time=5, repeat_time=1):
    text = split(text, width)
    times_to_scroll = len(text)
    for i in range(0,repeat_time):
        for j in range(0, times_to_scroll):
            LCD.lcd_display_string(" "*width, line)
            LCD.lcd_display_string(text[j], line)
            sleep(pause_time)

def smooth_scroll(LCD, width, text, line, pause_time=1, repeat_time=1):
    for j in range(0, repeat_time):
        for i in range(0, len(text)):
            LCD.lcd_display_string(text[0+i:width+i], line)
            sleep(pause_time)
            if i == len(text)-width:
                sleep(pause_time + 0.2)
                break
