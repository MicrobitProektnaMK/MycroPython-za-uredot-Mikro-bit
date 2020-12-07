from microbit import *                                      

pinovi = [pin0, pin1, pin2]

while True:
    for i in range(0, 3):
        pinovi[i].write_digital(1)
        sleep(100)
        pinovi[i].write_digital(0)
        sleep(100)
