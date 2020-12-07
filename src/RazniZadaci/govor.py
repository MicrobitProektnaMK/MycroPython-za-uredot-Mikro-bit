from microbit import *                                      
import speech

while True: 
    if button_a.is_pressed():
        speech.say("dobar dan!")
    if button_b.is_pressed():
        speech.say("dovidjenja!")
