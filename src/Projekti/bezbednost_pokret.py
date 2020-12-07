from microbit import *                                      
import radio

radio.on()

while True:
    dvizenje = pin0.read_digital()
    if dvizenje == 1:
        radio.send("dvizenje")
    sleep(1000)


