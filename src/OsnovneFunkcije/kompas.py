from microbit import *                                      

compass.calibrate()

while True:

    agol = compass.heading()
    
    if agol > 45 and agol <= 135:
        display.show("E") 
    elif agol > 135 and agol <= 225:
        display.show("S") 
    elif agol > 225 and agol <= 315:
        display.show("W") 
    else:
        display.show("N") 
    
    sleep(100)
