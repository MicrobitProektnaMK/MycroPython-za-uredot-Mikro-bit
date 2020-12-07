from microbit import *

while True:
    # crveno
    pin0.write_digital(1)
    pin1.write_digital(0)
    sleep(7000)

    # crveno+zolto
    pin1.write_digital(1)
    sleep(3000)

    # zeleno
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(7000)

    # zolto
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(3000)