from microbit import *                                      

while True:
    if button_a.is_pressed():
        temp = temperature()
        display.scroll("Temperaturata e:" + str(temp) + " C")
    sleep(100)
