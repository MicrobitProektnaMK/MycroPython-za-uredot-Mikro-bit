from microbit import *                                      
import random

list = Image("99999:90009:90009:90009:99999")
kamen = Image("00000:09990:09990:09990:00000")
nozicki = Image("99009:99090:00900:99090:99009")

sliki = [list, kamen, nozicki]

while True:
    dvizanje = accelerometer.current_gesture()
    if dvizanje == "shake":
        display.show(random.choice(sliki))
