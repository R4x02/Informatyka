ciagi = []
with open("ciagi.txt", "r") as plik:
    for linia in plik.readlines():
        ciagi.append(linia.strip())
# print(ciagi)
for i in range(len(ciagi)):
    if ciagi[i][0:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])
licznik = 0 
for i in range(len(ciagi)):
    if not '11' in ciagi[i]:
        licznik += 1
print(licznik)

liczbyDz=[]
def horner(liczba, x):  
    W = int(liczba[0])
    for i in range(1,len(liczba)):
        W = W * x + int(liczba[i])
    return W
for i in range (len(ciagi)):
    liczbyDz.append(horner(ciagi[i],2))
# print(liczbyDz)
liczbyPierwsze = []
liczby = []
for i in range(270000):
    liczby.append(1)
for i in range(2,270000):
    if liczby[i] == 1:
        for j in range(i + i, 270000,i):
            liczby[j]=0
for i in range(2,270000):
    if liczby[i] == 1:
        liczbyPierwsze.append(i)
# print(liczbyPierwsze)
for i in range(len(liczbyDz)):
    liczba = liczbyDz[i]
    czynniki=[]
    for j in range(len(liczbyPierwsze)):
        while(liczba%liczbyPierwsze[j] == 0):
            liczba = liczba  // liczbyPierwsze[j]
            czynniki.append(liczbyPierwsze[j])
        if len(czynniki)>2:
            break
    else:
        if len(czynniki)==2:
            print(liczbyDz[i],czynniki)