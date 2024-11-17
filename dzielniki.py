lista = []
with open("liczby.txt", "r") as plik:
    for linia in plik.readlines():
        lista.append(int(linia))

licznik = 0
L1 = 0
L2 = 0
for i in lista:
    if i<1000:
        licznik += 1
        L1 = L2
        L2 = i
print(licznik, L1, L2)

def licz_dzielniki(a):
    dzielniki = []
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            dzielniki.append(i)
            if i != a // i:
                dzielniki.append(a // i)
    dzielniki.sort()
    return dzielniki

for a in lista:
    dzielniki = licz_dzielniki(a)
    if len(dzielniki) == 18:
        print(a)
        print(*dzielniki)

def nwd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

najwieksza = 0

for i in range(len(lista)):
    ok = True
    for j in range(len(lista)):
        if i != j and nwd(lista[i], lista[j]) > 1:
            ok = False
            break
    if ok and lista[i] > najwieksza:
        najwieksza = lista[i]

print(najwieksza)
