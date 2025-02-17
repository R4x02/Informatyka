def suma_cyfr(liczba):
    suma = 0
    for cyfra in str(liczba):
        suma += int(cyfra)
    return suma


def pierwsza(liczba):
    if liczba < 2:
        return False
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    for i in range(3, int(liczba ** 0.5) + 1, 2):
        if liczba % i == 0:
            return False
    return True


def czy_trojkat(a, b, c):
    return a + b > c and a + c > b and b + c > a


def czy_prostokatny(a, b, c):
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2


lista_trojek = []
with open("trojki.txt") as plik:
    for linia in plik:
        lista_trojek.append(list(map(int, linia.split())))

wyniki_66_1 = []
for trojka in lista_trojek:
    if suma_cyfr(trojka[0]) + suma_cyfr(trojka[1]) == trojka[2]:
        wyniki_66_1.append(trojka)

wyniki_66_2 = []
for trojka in lista_trojek:
    if pierwsza(trojka[0]) and pierwsza(trojka[1]) and trojka[0] * trojka[1] == trojka[2]:
        wyniki_66_2.append(trojka)

wyniki_66_3 = []
for i in range(len(lista_trojek) - 1):
    trojka1 = lista_trojek[i]
    trojka2 = lista_trojek[i + 1]
    if czy_prostokatny(trojka1[0], trojka1[1], trojka1[2]) and czy_prostokatny(trojka2[0], trojka2[1], trojka2[2]):
        wyniki_66_3.append((trojka1, trojka2))

licznik_trojkatnych = 0
najdluzszy_ciag = 0
aktualny_ciag = 0
for trojka in lista_trojek:
    if czy_trojkat(trojka[0], trojka[1], trojka[2]):
        licznik_trojkatnych += 1
        aktualny_ciag += 1
        if aktualny_ciag > najdluzszy_ciag:
            najdluzszy_ciag = aktualny_ciag
    else:
        aktualny_ciag = 0

with open("wyniki_trojki.txt", "w", encoding="utf-8") as plik_wynikowy:
    plik_wynikowy.write("66.1\n")
    for trojka in wyniki_66_1:
        plik_wynikowy.write(f"{trojka[0]} {trojka[1]} {trojka[2]}\n")

    plik_wynikowy.write("66.2\n")
    for trojka in wyniki_66_2:
        plik_wynikowy.write(f"{trojka[0]} {trojka[1]} {trojka[2]}\n")

    plik_wynikowy.write("66.3\n")
    for para in wyniki_66_3:
        plik_wynikowy.write(f"{para[0][0]} {para[0][1]} {para[0][2]} | {para[1][0]} {para[1][1]} {para[1][2]}\n")

    plik_wynikowy.write("66.4\n")
    plik_wynikowy.write(f"Liczba wierszy trojkatnych: {licznik_trojkatnych}\n")
    plik_wynikowy.write(f"Najdluzszy ciag trojkatny: {najdluzszy_ciag}\n")