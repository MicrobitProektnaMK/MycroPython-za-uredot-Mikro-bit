from microbit import *                                      

korak = 1
osvetljaj = 0

while True:
    display.set_pixel(2, 2, osvetljaj)
    osvetljaj += korak
    sleep(200)
    if osvetljaj == 9 or osvetljaj == 0:  
        korak = -korak
