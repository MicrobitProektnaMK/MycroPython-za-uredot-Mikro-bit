from microbit import *                                      
import radio

radio.on()

while True:
    if button_a.is_pressed():
        radio.send("L")
        display.show(Image.ARROW_W)
        sleep(3000)
    if button_b.is_pressed():
        radio.send("D")
        display.show(Image.ARROW_E)
        sleep(3000)



    display.clear()