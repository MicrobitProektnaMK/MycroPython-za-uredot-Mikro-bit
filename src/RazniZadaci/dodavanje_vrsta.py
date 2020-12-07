from microbit import *                                      

while True:

    vrednost = pin0.read_analog()

    if vrednost > 900:
        for i in range(0, 5):
            display.set_pixel(i, 0, 5)
    if vrednost > 700:
        for i in range(0, 5):
            display.set_pixel(i, 1, 5)
    if vrednost > 500:
        for i in range(0, 5):
            display.set_pixel(i, 2, 5)
    if vrednost > 300:
        for i in range(0, 5):
            display.set_pixel(i, 3, 5)
    if vrednost > 100:
        for i in range(0, 5):
            display.set_pixel(i, 4, 5)
    sleep(50)
    display.clear()