from microbit import *                                      
import radio

radio.on()
broj = 0

while True:
    display.show(str(broj))
    if button_a.was_pressed():
        broj += 1
    if button_b.was_pressed():
        broj -= 1
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(str(broj))
    sleep(500)