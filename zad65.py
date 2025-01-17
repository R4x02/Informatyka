def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

with open("informatyka/dane/65/dane_ulamki.txt", "r") as file:
    dane = [line.strip().split() for line in file]
    dane = [(int(x[0]), int(x[1])) for x in dane]

min_ulamek = dane[0]
for licz, mian in dane[1:]:
    if licz * min_ulamek[1] < min_ulamek[0] * mian or \
       (licz * min_ulamek[1] == min_ulamek[0] * mian and mian < min_ulamek[1]):
        min_ulamek = (licz, mian)

nieskracalne = 0
for licz, mian in dane:
    if nwd(licz, mian) == 1:
        nieskracalne += 1

suma_licznikow = 0
for licz, mian in dane:
    gcd = nwd(licz, mian)
    suma_licznikow += licz // gcd

b = 2**2 * 3**2 * 5**2 * 7**2 * 13
suma_licznikow_b = 0
for licz, mian in dane:
    suma_licznikow_b += licz * (b // mian)

print(f"Zadanie 1: {min_ulamek[0]} {min_ulamek[1]}\n")
print(f"Zadanie 2: {nieskracalne}\n")
print(f"Zadanie 3: {suma_licznikow}\n")
print(f"Zadanie 4: {suma_licznikow_b}\n")