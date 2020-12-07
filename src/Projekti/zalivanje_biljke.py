from microbit import *                                      

while True:
    vlaznost = pin0.read_analog()//10
    if vlaznost < 80:
        pin1.write_digital(1)
        sleep(1000)
        pin1.write_digital(0)
        sleep(3000)
    else:
        sleep(10000)
    if button_a.is_pressed():
        display.scroll(str(vlaznost))
        sleep(1000)