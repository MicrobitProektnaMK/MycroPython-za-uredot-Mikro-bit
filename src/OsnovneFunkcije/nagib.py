from microbit import *

while True:
    naklon = accelerometer.get_x()
    if naklon > 40:
        display.show("D")
    elif naklon < -40:
        display.show("L")
    else:
        display.show("-")