from microbit import *                                      
import music 

ukljucen = False

while True: 

    print(accelerometer.get_x())  # ako želimo da pratimo vrednosti x u REPL
    if button_a.was_pressed():
        ukljucen = True
    if button_b.was_pressed():
        ukljucen = False

    if ukljucen and abs(accelerometer.get_x()) > 100:
        music.pitch(1000, 100)
        music.pitch(500, 100)
