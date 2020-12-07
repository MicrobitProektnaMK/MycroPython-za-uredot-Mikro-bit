from microbit import *                                      

# signali ce trajati po 20 milisekundi
pin0.set_analog_period(20)

while True:
    if button_a.is_pressed():
        pin0.write_analog(160) # podizanje rampe
    if button_b.is_pressed():
        pin0.write_analog(60) # spustanje rampe
