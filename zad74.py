lista = []
with open("hasla.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        lista.append(linia.strip())
print(lista)

ile = 0
for haslo in lista:
    if haslo.isdecimal():
        ile += 1
print(ile)

slownik = {}
for haslo in lista:
    if haslo in slownik:
        slownik[haslo] += 1
    else:
        slownik[haslo] = 1
for x, y in slownik.items():
    if y > 1:
        print(x)

liczba_zlozonych = 0
for haslo in lista:
    zawiera_cyfre = False
    zawiera_mala = False
    zawiera_duza = False
    for znak in haslo:
        if znak.isdigit():
            zawiera_cyfre = True
        if znak.islower():
            zawiera_mala = True
        if znak.isupper():
            zawiera_duza = True
    if zawiera_cyfre and zawiera_mala and zawiera_duza:
        liczba_zlozonych += 1

print(liczba_zlozonych)