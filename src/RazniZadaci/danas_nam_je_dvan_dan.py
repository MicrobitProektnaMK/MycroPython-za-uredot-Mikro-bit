import music                                                

danas_nam_je = ["G4:4", "G", "E", "C", "A", "A", "G:8", "F:4", "F", "E:8",
         "D:4", "D", "C:8"]
ziveo_ziveo = ["A4:4", "F", "A:8", "G:4", "E", "G:8", "F:4", "F", "E", "D", ]
bi_i_oo = ["E", "F", "G:8"]
bii_o = ["C:8", "C:4"]

for i in range(2):  # prva dva stiha imaju iste note
    music.play(danas_nam_je) 
music.play(ziveo_ziveo)
music.play(bi_i_oo)
music.play(ziveo_ziveo)
music.play(bii_o)
