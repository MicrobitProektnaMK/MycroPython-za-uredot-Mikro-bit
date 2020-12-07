from microbit import *                                      
import radio

radio.on()

while True:
    svrti = radio.receive()
    if svrti is not None:
        if svrti == "D":
            for i in range(4):
                display.show(Image.ARROW_E)
                sleep(1000)
                display.clear()
                sleep(500)