from microbit import *                                      
from utime import ticks_us, sleep_us, ticks_diff

def rastojanie():
    pin0.write_digital(0)
    sleep_us(10)
    pin0.write_digital(1)
    sleep_us(10)
    pin0.write_digital(0)

    while pin1.read_digital() == 0:
        pass
    start = ticks_us()

    while pin1.read_digital() == 1:
        pass
    end = ticks_us()

    cm = ticks_diff(end, start) // 58
    return cm

while True:
    display.scroll(rastojanie())
    sleep(1000)