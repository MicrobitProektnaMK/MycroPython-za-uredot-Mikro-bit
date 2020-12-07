from microbit import *                                      

brod1 = Image("50000:50000:50000:99000:90000")
brod2 = Image("05000:05000:05000:99900:99000")
brod3 = Image("50500:50500:50500:99990:99900")
brod4 = Image("05050:05050:05050:99999:09990")
brod5 = Image("00505:00505:00505:09999:00999")
brod6 = Image("00050:00050:00050:00999:00099")
brod7 = Image("00005:00005:00005:00099:00009")
brod8 = Image("00000:00000:00000:00009:00000")
brod9 = Image("00000:00000:00000:00000:00000")

brodovi = [brod1, brod2, brod3, brod4, brod5, brod6, brod7, brod8, brod9]

while True:
    display.show(brodovi, delay=500)
