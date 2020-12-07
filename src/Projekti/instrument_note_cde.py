from microbit import *                                      
import radio

radio.on()
while True:
    if pin0.is_touched():
        radio.send("C4")
        sleep(500)
    elif pin1.is_touched():
        radio.send("D4")
        sleep(500)
    elif pin2.is_touched():
        radio.send("E4")
        sleep(500)
