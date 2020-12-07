from microbit import *                                      
import radio

radio.on()

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        radio.send("frlanje")
    if button_a.was_pressed():
        radio.send("sleden igrac")