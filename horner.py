def horner(liczba, podstawa):
    dziesietny = int(liczba[0])
    for i in range(1, len(liczba)):
        dziesietny = dziesietny * podstawa + int(liczba[i])
    return dziesietny

def konwertuj_na_system(liczba, system):
    wynik = ""
    while liczba > 0:
        reszta = liczba % system
        if reszta >= 10:
            wynik = chr(55 + reszta) + wynik
        else:
            wynik = str(reszta) + wynik
        liczba //= system
    return wynik

def zlicz_szesci(liczba_str):
    return liczba_str.count('6')

# Zadanie 1
lista_liczb1 = []
with open("liczby1.txt", "r") as plik1:
    for linia in plik1.readlines():
        lista_liczb1.append(linia.strip())

maksymalna_wartosc = -1
minimalna_wartosc = float('inf')
maksymalna_liczba = ""
minimalna_liczba = ""

for liczba in lista_liczb1:
    wartosc_dziesietna = horner(liczba, 8)
    if wartosc_dziesietna > maksymalna_wartosc:
        maksymalna_wartosc = wartosc_dziesietna
        maksymalna_liczba = liczba
    if wartosc_dziesietna < minimalna_wartosc:
        minimalna_wartosc = wartosc_dziesietna
        minimalna_liczba = liczba

maksymalna_wartosc_octal = konwertuj_na_system(maksymalna_wartosc, 8)
minimalna_wartosc_octal = konwertuj_na_system(minimalna_wartosc, 8)

# Zadanie 2
lista_liczb2 = []
with open("liczby2.txt", "r") as plik2:
    for linia in plik2.readlines():
        lista_liczb2.append(int(linia.strip()))

najdluzszy_ciag = 0
aktualna_dlugosc = 1
pierwszy_element = lista_liczb2[0]
aktualny_poczatek = lista_liczb2[0]

for i in range(1, len(lista_liczb2)):
    if lista_liczb2[i] >= lista_liczb2[i - 1]:
        aktualna_dlugosc += 1
    else:
        if aktualna_dlugosc > najdluzszy_ciag:
            najdluzszy_ciag = aktualna_dlugosc
            pierwszy_element = aktualny_poczatek
        aktualna_dlugosc = 1
        aktualny_poczatek = lista_liczb2[i]

if aktualna_dlugosc > najdluzszy_ciag:
    najdluzszy_ciag = aktualna_dlugosc
    pierwszy_element = aktualny_poczatek

# Zadanie 3
lista_liczb1_dec = [int(liczba, 8) for liczba in lista_liczb1]
lista_liczb2_dec = lista_liczb2

ilosc_takich_samych = 0
ilosc_wiekszych_w_liczby1 = 0

for liczba1, liczba2 in zip(lista_liczb1_dec, lista_liczb2_dec):
    if liczba1 == liczba2:
        ilosc_takich_samych += 1
    elif liczba1 > liczba2:
        ilosc_wiekszych_w_liczby1 += 1

# Zadanie 4
liczba_szesci_w_dziesietnym = 0
liczba_szesci_w_osemkowym = 0

for liczba in lista_liczb2:
    liczba_szesci_w_dziesietnym += zlicz_szesci(str(liczba))

    liczba_osemkowy = ""
    temp = liczba
    while temp > 0:
        liczba_osemkowy = str(temp % 8) + liczba_osemkowy
        temp //= 8

    liczba_szesci_w_osemkowym += zlicz_szesci(liczba_osemkowy)

with open("wyniki.txt", "w", encoding="utf-8") as wyniki:
    wyniki.write(f"Zadanie 1:\n")
    wyniki.write(f"Maksymalna liczba w systemie ósemkowym: {maksymalna_wartosc_octal}\n")
    wyniki.write(f"Minimalna liczba w systemie ósemkowym: {minimalna_wartosc_octal}\n\n")

    wyniki.write(f"Zadanie 2:\n")
    wyniki.write(f"Pierwszy element najdłuższego niemalejącego ciągu: {pierwszy_element}\n")
    wyniki.write(f"Długość najdłuższego ciągu: {najdluzszy_ciag}\n\n")

    wyniki.write(f"Zadanie 3:\n")
    wyniki.write(f"Liczby takie same: {ilosc_takich_samych}\n")
    wyniki.write(f"Liczby w liczby1 większe niż w liczby2: {ilosc_wiekszych_w_liczby1}\n\n")

    wyniki.write(f"Zadanie 4:\n")
    wyniki.write(f"Cyfra 6 występuje {liczba_szesci_w_osemkowym} razy w systemie dziesiętnym i  {liczba_szesci_w_dziesietnym} razy w systemie ósemkowym\n")

