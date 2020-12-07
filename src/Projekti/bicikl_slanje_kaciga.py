from microbit import *                                      
import radio

radio.on()

while True:
    stranicno__dvizenje = accelerometer.get_x()
    if stranicno__dvizenje > 300: # koga ja navednuvame glavata nalevo
        radio.send("L")
        # gledano od prednata strana, nalevo pokazuva strelkata ARROW_E
        display.show(Image.ARROW_E)
        sleep(3000)
    if stranicno__dvizenje < -300: # koga ja navednuvame glavata nadesno
        radio.send("D")
        # gledano od prednata strana, nadesno pokazuva strelkata ARROW_W
        display.show(Image.ARROW_W)
        sleep(3000)
    display.clear()