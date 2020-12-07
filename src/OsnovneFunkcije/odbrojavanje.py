from microbit import *

for broj in range(5, -1, -1):
    display.show(str(broj))
    sleep(1000)
display.show(Image.DIAMOND)