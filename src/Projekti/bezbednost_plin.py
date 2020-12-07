from microbit import *                                      
import radio

radio.on()

while True:
    plin = pin1.read_analog()
    if plin > 500:
        radio.send("plin")
    sleep(1000)





