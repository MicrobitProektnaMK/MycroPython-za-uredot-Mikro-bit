from microbit import *                                      

while True:
    svetlo = display.read_light_level()
    if button_b.was_pressed():
        display.scroll(str(svetlo))

    if svetlo < 20:
        display.show(Image.CHESSBOARD)
        sleep(500)
        display.clear()
        sleep(500)
    else:
        display.clear()
