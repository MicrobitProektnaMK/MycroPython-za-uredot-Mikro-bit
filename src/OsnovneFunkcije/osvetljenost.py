from microbit import *                                      

while True:
    svetlo = display.read_light_level()
    display.scroll(str(svetlo))
    sleep(500)
