from microbit import *                                      

while True:
    c = temperature()
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll(str(c*1.8+32) + ' F')
    elif button_a.is_pressed():
        display.scroll(str(c) + ' C')
    elif button_b.is_pressed():
        display.scroll(str(c + 273.15) + ' K')
    sleep(100)
