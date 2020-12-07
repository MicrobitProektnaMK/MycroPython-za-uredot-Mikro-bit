from microbit import *                                      
import radio

radio.on()

while True:
    if button_a.was_pressed():
        display.scroll("Dobredojdovte")
        radio.send("vlez")
    sleep(1000)
