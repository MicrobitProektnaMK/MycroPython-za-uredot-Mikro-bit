import music                                                

na_krajot_od_seloto = ['E4:4', 'F', 'G', 'G']
zolta_kukja = na_krajot_od_seloto
ta_ta_ta = ['E4:4', 'F', 'G:8']
zolta_kukjicka = ['G4:4', 'G', 'F', 'F', 'E:8']

music.play(na_krajot_od_seloto)
for i in range(2):
    music.play(zolta_kukja)
    music.play(ta_ta_ta)
music.play(zolta_kukjicka)
