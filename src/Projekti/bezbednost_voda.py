from microbit import *                                      
import radio

radio.on()

while True:
    voda = pin2.read_digital()
    if voda == 0:
        radio.send("voda")
    sleep(1000)