from microbit import *                                      
import music
import radio

radio.on()
while True:
    nota = radio.receive()
    if nota is not None:
        music.play(nota)
        nota = nota[0]
        if nota == "B":
            nota = "H"
        display.show(nota)

