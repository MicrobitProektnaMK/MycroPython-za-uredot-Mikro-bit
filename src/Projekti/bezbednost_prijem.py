from microbit import *                                      
import radio

vklucen = False

while True:
    if button_a.is_pressed():
        vklucen = True
        radio.on()

    if button_b.was_pressed():
        vklucen = False
        radio.off()

    if vklucen:
        poraka = radio.receive()
        if poraka is not None:
            for i in range(10):
                music.pitch(1000, 100)
                music.pitch(500, 100)
            display.scroll(str(poraka))