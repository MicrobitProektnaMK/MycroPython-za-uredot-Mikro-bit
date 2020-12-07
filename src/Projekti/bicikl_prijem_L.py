from microbit import *                                      
import radio

radio.on()

while True:
    svrti = radio.receive()
    if svrti is not None:
        if svrti == "L":
            for i in range(4):
                display.show(Image.ARROW_W)
                sleep(1000)
                display.clear()
                sleep(500)