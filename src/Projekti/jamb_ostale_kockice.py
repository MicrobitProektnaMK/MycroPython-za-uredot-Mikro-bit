from microbit import *                                      
import random
import radio

radio.on()
prethodniot_broj_se_zacuvuva  = False

while True:
    if button_a.was_pressed():
        prethodniot_broj_se_zacuvuva  = True

    primena_poraka = radio.receive()
    if primena_poraka is not None:
        if primena_poraka == "sleden igrac":
            prethodniot_broj_se_zacuvuva  = False
        elif primena_poraka == "frlanje":
            if not prethodniot_broj_se_zacuvuva :
                broj = random.randint(1, 6)
                display.show(str(broj))