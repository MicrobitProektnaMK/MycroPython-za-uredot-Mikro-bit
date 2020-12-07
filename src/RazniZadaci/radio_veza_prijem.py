from microbit import *                                      
import radio

radio.on()

while True:
    dioda = radio.receive()
    if dioda is not None:
        if dioda == "1":
            pin1.write_digital(1)
        if dioda == "0":
            pin1.write_digital(0)
        sleep(100)
