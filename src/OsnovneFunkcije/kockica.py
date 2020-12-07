import random                                               
from microbit import *

while True:
    broj = random.randint(1, 6)
    display.show(str(broj))
    if button_a.is_pressed():
        sleep(5000)
