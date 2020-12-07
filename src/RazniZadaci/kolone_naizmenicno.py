from microbit import *                                      

def postavi_kolone(kolona1, kolona2, osvetljenost):
    for red in range(5):
        display.set_pixel(kolona1, red, osvetljenost)
        display.set_pixel(kolona2, red, osvetljenost)
    sleep(500)

while True:
    postavi_kolone(0, 1, 9) # ukljuci prve dve kolone
    postavi_kolone(0, 1, 0) # iskljuci prve dve kolone
    postavi_kolone(3, 4, 9) # ukljuci poslednje dve kolone
    postavi_kolone(3, 4, 0) # iskljuci poslednje dve kolone
