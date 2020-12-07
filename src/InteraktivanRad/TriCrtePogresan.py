from microbit import *                                      

for x in range(0, 5, 2):
    for y in range(5, 2, -1):
        display.set_pixel(x, y, 5)
