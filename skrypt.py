ciagi = []
with open("ciagi.txt", "r") as plik:
    zawartosc = plik.readlines()
    i = 0
    while i < len(zawartosc):
        liczba_wyrazow = int(zawartosc[i].strip())
        ciag = [int(x) for x in zawartosc[i + 1].strip().split()]
        ciagi.append(ciag)
        i += 2

bledne_ciagi = []
with open("bledne.txt", "r") as bledne_plik:
    zawartosc = bledne_plik.readlines()
    i = 0
    while i < len(zawartosc):
        liczba_wyrazow = int(zawartosc[i].strip())
        ciag = [int(x) for x in zawartosc[i + 1].strip().split()]
        bledne_ciagi.append(ciag)
        i += 2

liczba_arytmetycznych = 0
max_roznica = 0

for c in ciagi:
    roznica = c[1] - c[0]
    czy_arytmetyczny = True
    for i in range(2, len(c)):
        if c[i] - c[i - 1] != roznica:
            czy_arytmetyczny = False
            break
    if czy_arytmetyczny:
        liczba_arytmetycznych += 1
        if roznica > max_roznica:
            max_roznica = roznica

with open("wynik1.txt", "w") as wynik1:
    wynik1.write(str(liczba_arytmetycznych) + "\n")
    wynik1.write(str(max_roznica) + "\n")

szesciany = set()
n = 1
while n**3 <= 1000000:
    szesciany.add(n**3)
    n += 1

najwieksze_szesciany = []
for c in ciagi:
    najwiekszy_szescian = None
    for x in c:
        if x in szesciany and (najwiekszy_szescian is None or x > najwiekszy_szescian):
            najwiekszy_szescian = x
    if najwiekszy_szescian is not None:
        najwieksze_szesciany.append(najwiekszy_szescian)

with open("wynik2.txt", "w") as wynik2:
    for szescian in najwieksze_szesciany:
        wynik2.write(str(szescian) + "\n")

bledne_wyrazy = []
for c in bledne_ciagi:
    roznice = []
    for i in range(1, len(c)):
        roznice.append(c[i] - c[i - 1])
    
    licznik = {}
    for r in roznice:
        if r in licznik:
            licznik[r] += 1
        else:
            licznik[r] = 1
    prawidlowa_roznica = max(licznik, key=licznik.get)

    for i in range(1, len(c)):
        if c[i] - c[i - 1] != prawidlowa_roznica:
            bledne_wyrazy.append(c[i])
            break

with open("wynik3.txt", "w") as wynik3:
    for wyraz in bledne_wyrazy:
        wynik3.write(str(wyraz) + "\n")
