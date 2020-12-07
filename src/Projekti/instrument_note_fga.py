from microbit import *                                      
import radio

radio.on()
while True:
    if pin0.is_touched():
        radio.send("F4")
        sleep(500)
    elif pin1.is_touched():
        radio.send("G4")
        sleep(500)
    elif pin2.is_touched():
        radio.send("A4")
        sleep(500)
