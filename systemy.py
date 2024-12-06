def horner(liczba, x):  # liczba - string, x - system
    W = int(liczba[0])
    for i in range(1,len(liczba)):
        W = W * x + int(liczba[i])
    return W
print(horner("11010", 2))

def decToALL(liczba,x):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % x) + wynik 
        liczba = liczba // x
    return wynik 

print(decToALL(449,8))



