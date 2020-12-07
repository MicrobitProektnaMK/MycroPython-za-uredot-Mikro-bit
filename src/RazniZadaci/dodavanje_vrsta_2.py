from microbit import *                                      

while True:

    vrednost = pin0.read_analog()
    br_vrsta = (vrednost + 100) // 200
    for x in range(5):
        for y in range(5 - br_vrsta, 5):
            display.set_pixel(x, y, 5)
    sleep(50)
    display.clear()
