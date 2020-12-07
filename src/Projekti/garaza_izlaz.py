from microbit import *                                      
import radio

radio.on()

while True:
    if button_a.was_pressed():
        radio.send("izlez")
        display.scroll("Srekjen pat!")
    sleep(1000)
