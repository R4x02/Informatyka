def funkcja(x):
    return 2 * x - 2

def znajdz_punkt_zerowy(lewa_granica, prawa_granica, dokladnosc):
    if funkcja(lewa_granica) * funkcja(prawa_granica) > 0:
        return None
    while True:
        srodek = (lewa_granica + prawa_granica) / 2
        if funkcja(srodek) == 0:
            return srodek
        if funkcja(lewa_granica) * funkcja(srodek) < 0:
            prawa_granica = srodek
        else:
            lewa_granica = srodek
        if abs(prawa_granica - lewa_granica) < dokladnosc:
            return srodek

print(znajdz_punkt_zerowy(2, 6, 0.0001))
