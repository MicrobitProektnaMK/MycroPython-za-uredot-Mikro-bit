import music                                                

while True:
    for frekv in range(880, 1760, 16):
        music.pitch(frekv, 15)
    for frekv in range(1760, 880, -16):
        music.pitch(frekv, 15)
