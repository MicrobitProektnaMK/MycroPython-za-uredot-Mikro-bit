from microbit import *                                      

while True:
    #vrednost = pin0.read_analog()
    vrednost = int(input())
    display.clear()
    br_na_redovi = (vrednost + 100) // 200
    for x in range(5):
        for y in range(5 - br_na_redovi, 5):
            display.set_pixel(x, y, 5)
    sleep(50)
