from microbit import *                                      
import random

br1 = Image("00000:00000:00900:00000:00000")
br2 = Image("00000:09000:00000:00090:00000")
br3 = Image("00000:09000:00900:00090:00000")
br4 = Image("00000:09090:00000:09090:00000")
br5 = Image("00000:09090:00900:09090:00000")
br6 = Image("00000:09090:09090:09090:00000")
brojevi = [br1, br2, br3, br4, br5, br6]
while True:
    if accelerometer.is_gesture('shake'):
        n = random.randint(0, 5)
        display.show(brojevi[n])