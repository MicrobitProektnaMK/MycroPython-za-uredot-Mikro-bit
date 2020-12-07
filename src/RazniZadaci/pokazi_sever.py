from microbit import *                                      

compass.calibrate()
while True:
    ugao = compass.heading()
    if ugao > 45 and ugao <= 135: 
        # azimut ~ istok -> ukljuci LED na sredini leve ivice
        display.set_pixel(0, 2, 9)
    elif ugao > 135 and ugao <= 225: # jug
        # azimut ~ jug -> ukljuci LED na sredini donje ivice
        display.set_pixel(2, 4, 9)
    elif ugao > 225 and ugao <= 315:
        # azimut ~ zapad -> ukljuci LED na sredini desne ivice
        display.set_pixel(4, 2, 9)
    else:
        # azimut ~ sever -> ukljuci LED na sredini gornje ivice
        display.set_pixel(2, 0, 9)
    sleep(100)
    display.clear()
