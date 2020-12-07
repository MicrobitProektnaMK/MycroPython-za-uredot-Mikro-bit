from microbit import *

while True:
    osvetljaj = pin0.read_analog()
    print(osvetljaj)  # za posmatranje vrednosti
    if osvetljaj > 400:
        pin1.write_digital(0)
        display.scroll("dan")
    else:
        pin1.write_digital(1)
        display.scroll("noc")
    sleep(200)