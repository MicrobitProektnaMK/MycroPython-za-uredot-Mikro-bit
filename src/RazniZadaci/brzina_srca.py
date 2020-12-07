from microbit import *                                      

while True:
    pauza = pin0.read_analog()+50
    display.show(Image.HEART)
    sleep(pauza)
    display.clear()
    sleep(pauza)
