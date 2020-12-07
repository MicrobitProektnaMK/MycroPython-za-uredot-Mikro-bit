from microbit import *                                      

while True:

    for osvetljaj in range(10):
        display.set_pixel(2, 2, osvetljaj)
        sleep(200)  
    for osvetljaj in range(9, 0, -1):
        display.set_pixel(2, 2, osvetljaj)
        sleep(200)
