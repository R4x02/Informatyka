def czy_anagramy(napis_a, napis_b):
	return len(napis_a) == len(napis_b) and sorted(napis_a) == sorted(napis_b)

def czy_jednolity(napis):
	return all(litera == napis[0] for litera in napis)

def policz_jednolite_anagramy(linie):
	licznik = 0
	for linia in linie:
		a, b = linia.split()
		if len(a) == len(b) and czy_jednolity(a) and czy_jednolity(b) and czy_anagramy(a, b):
			licznik += 1
	return licznik

def policz_pary_anagramow(linie):
	licznik = 0
	for linia in linie:
		a, b = linia.split()
		if czy_anagramy(a, b):
			licznik += 1
	return licznik

def znajdz_maksymalne_k(linie):
	grupy_anagramow = {}
	for linia in linie:
		a, b = linia.split()
		klucz_a = ''.join(sorted(a))
		klucz_b = ''.join(sorted(b))
		if klucz_a not in grupy_anagramow:
			grupy_anagramow[klucz_a] = set()
		if klucz_b not in grupy_anagramow:
			grupy_anagramow[klucz_b] = set()
		grupy_anagramow[klucz_a].add(a)
		grupy_anagramow[klucz_a].add(b)
		grupy_anagramow[klucz_b].add(a)
		grupy_anagramow[klucz_b].add(b)
	return max((len(grupa) for grupa in grupy_anagramow.values()), default=0)

with open('dane_napisy.txt', 'r') as plik:
	linie = plik.readlines()

	wyniki_68_1 = policz_jednolite_anagramy(linie)
	wyniki_68_2 = policz_pary_anagramow(linie)
	wyniki_68_3 = znajdz_maksymalne_k(linie)

	with open('wyniki_anagramy.txt', 'w') as plik_wynikowy:
		plik_wynikowy.write("68.1\n")
		plik_wynikowy.write(f"{wyniki_68_1}\n")
		plik_wynikowy.write("68.2\n")
		plik_wynikowy.write(f"{wyniki_68_2}\n")
		plik_wynikowy.write("68.3\n")
		plik_wynikowy.write(f"{wyniki_68_3}\n")
