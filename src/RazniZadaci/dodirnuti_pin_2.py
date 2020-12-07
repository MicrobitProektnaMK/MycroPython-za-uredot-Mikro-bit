from microbit import *                                      

pinovi = (pin0, pin1, pin2)

while True:
    for i in range(3):
        if pinovi[i].is_touched():
            display.show(i)
