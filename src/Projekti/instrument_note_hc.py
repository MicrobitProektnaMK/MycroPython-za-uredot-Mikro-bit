from microbit import *                                      
import radio

radio.on()
while True:
    if pin0.is_touched():
        radio.send("B4")
        sleep(500)
    elif pin1.is_touched():
        radio.send("C5")
        sleep(500)



