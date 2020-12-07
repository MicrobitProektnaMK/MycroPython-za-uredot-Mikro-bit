from microbit import *                                      
display.show(Image.DIAMOND)
while True:
    for y in range(5):
        for x in range(5):
            n = display.get_pixel(x, y)
            print('red', y, 'kol', x, 'jacina', n)
            while True:
                if button_a.was_pressed():
                    n = (n + 1) % 10 # vrednosti od 0 do 9
                    display.set_pixel(x, y, n)
                    print('red', y, 'kol', x, 'jacina', n)
                elif button_b.was_pressed():
                    break
