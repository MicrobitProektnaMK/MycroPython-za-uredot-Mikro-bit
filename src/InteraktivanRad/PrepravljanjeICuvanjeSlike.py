from microbit import *                                      
display.show(Image.DIAMOND)
while True:
    for y in range(5):
        for x in range(5):
            n = display.get_pixel(x, y)
            print('red', y, 'kol', x, 'jacina', n)
            while True:
                if button_a.is_pressed() and button_b.is_pressed():
                    slika = []
                    for red in range(5):
                        red_slike = []
                        for kolona in range(5):
                            red_slike.append(str(display.get_pixel(kolona, red)))
                        slika.append(''.join(red_slike))
                    print(':'.join(slika))
                    sleep(2000)
                elif button_a.was_pressed():
                    n = (n + 1) % 10 # vrednosti od 0 do 9
                    display.set_pixel(x, y, n)
                    print('red', y, 'kol', x, 'jacina', n)
                elif button_b.was_pressed():
                    break
