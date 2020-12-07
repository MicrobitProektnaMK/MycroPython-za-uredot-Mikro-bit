from microbit import *                                      
import radio

radio.on()

while True:
    broj = radio.receive()
    if broj is not None:
        broj = int(broj)*5
        display.scroll(str(broj))
    sleep(100)