from microbit import *                                      
import radio

radio.on()

while True:
    otvorena_vrata = pin1.read_analog()
    if otvorena_vrata < 800:
        radio.send("vrata")
    sleep(500)