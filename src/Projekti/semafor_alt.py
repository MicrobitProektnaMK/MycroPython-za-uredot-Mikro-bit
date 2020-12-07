from microbit import *                                      

3
# Sekoja podterka vo terka 'podobro' pretstavuva opis na edna faza
# rabotenje_na semaforot, i toa: prvite tri broja po red kazuvaat dali
# crvena, zolto i zeleno se vkluceni vo taa faza,
# a cetvrtiot broj e traenje na fazata vo milisekundi
boje = (
    (1, 0, 0, 7000),  # crveno
    (1, 1, 0, 3000),  # crveno i zolto
    (0, 0, 1, 7000),  # zeleno
    (0, 1, 0, 3000)  # samo zolto
)
while True:
    for signal_za_crveno, signal_za_zolto, signal_za_zeleno, t in boje:
        pin0.write_digital(signal_za_crveno)
        pin1.write_digital(signal_za_zolto)
        pin2.write_digital(signal_za_zeleno)
        sleep(t)