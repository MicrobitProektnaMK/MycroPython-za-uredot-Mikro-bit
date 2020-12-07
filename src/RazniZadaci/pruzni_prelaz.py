from microbit import *                                      

while True:
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(500)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(500)
