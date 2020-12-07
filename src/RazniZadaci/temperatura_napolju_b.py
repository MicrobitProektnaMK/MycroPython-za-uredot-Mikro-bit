from microbit import *                                      
import radio

radio.on()

while True:
    temperatura = radio.receive()
    if temperatura is not None:
        temperatura = int(temperatura)  # pretvaramo dobijenu vrednost u broj
        print((temperatura,))  # Plotter radi samo sa torkama
        if temperatura < 20:
            display.scroll("hladno")
    sleep(2000)
