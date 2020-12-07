from microbit import *                                      
import radio

radio.on()

while True:
    if button_a.is_pressed():
        radio.send("1")
    if button_b.is_pressed():
        radio.send("0")
    sleep(100)
