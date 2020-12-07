from microbit import *                                      

while True:
    for i in range(0, 5):
        display.set_pixel(0, i, 9)  # prva kolona uključi
        display.set_pixel(1, i, 9)  # druga kolona uključi
    sleep(500)
    
    for i in range(0, 5):
        display.set_pixel(0, i, 0)  # prva kolona isključi
        display.set_pixel(1, i, 0)  # druga kolona isključi
    sleep(500)  
    
    for i in range(0, 5):
        display.set_pixel(3, i, 9)  # četvrta kolona uključi
        display.set_pixel(4, i, 9)  # peta kolona uključi 
    sleep(500)
    
    for i in range(0, 5):
        display.set_pixel(3, i, 0)  # četvrta kolona isključi
        display.set_pixel(4, i, 0)  # peta kolona isključi 
    sleep(500) 
