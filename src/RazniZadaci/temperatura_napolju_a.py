from microbit import *                                      
import radio

radio.on()

while True:
    temperatura = temperature()
    display.scroll(str(temperatura))
    radio.send(str(temperatura))
    sleep(1000)
