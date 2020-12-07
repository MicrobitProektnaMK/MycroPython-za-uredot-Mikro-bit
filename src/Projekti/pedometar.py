from microbit import *                                      

broj_na_cekori = 0
cilj = 3000

while True:
    if accelerometer.was_gesture('shake'):
        broj_na_cekori += 2
    if button_a.is_pressed():
        if broj_na_cekori < cilj:
            for x in range(3):
                display.show(Image.NO)
                sleep(200)
                display.clear()
                sleep(200)
        else:
            display.show(Image.HAPPY)
            sleep(200)

    if button_b.is_pressed():
        display.scroll(str(broj_na_cekori))
        sleep(200)




