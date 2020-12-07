from microbit import *                                      

osvetluvanje = 0
cekor = 10

while True:
    pin1.write_analog(osvetluvanje)
    osvetluvanje = osvetluvanje + cekor
    sleep(100)
    if osvetluvanje > 255 or osvetluvanje == 0:
        cekor = -cekor
