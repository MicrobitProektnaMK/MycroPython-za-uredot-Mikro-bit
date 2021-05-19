from microbit import *                                      
import radio

radio.on()

KAPACITET_NA_GARAZATA = 6
br_na_mesta = KAPACITET_NA_GARAZATA
pin0.set_analog_period(20)  # # za upravuvanje so pinot 0 - rampa

while True:
    if br_na_mesta > 0:
        display.show(str(br_na_mesta))
    else:
        display.scroll("Polna garaza!")

    poruka = radio.receive()
    if poruka == "vlez":
        if br_na_mesta > 0:
            pin0.write_analog(160)  # kreni ja rampata
            sleep(5000)
            pin0.write_analog(90)  # spusti ja rampata
            br_na_mesta -= 1
    elif poruka == "izlez":
        if br_na_mesta < KAPACITET_NA_GARAZATA:
            br_na_mesta += 1
    sleep(500)