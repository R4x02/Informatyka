def ile_yap_yap_yap(napis1, napis2):
	min_dlugosc = min(len(napis1), len(napis2))
	licznik = 0
	while licznik < min_dlugosc and napis1[-(licznik+1)] == napis2[-(licznik+1)]:
		licznik += 1
	return licznik

def zadanie_1(lista_napisow):
	licznik = 0
	pierwsza_para = None
	for napisy in lista_napisow:
		napis1, napis2 = napisy
		if len(napis1) > 3 * len(napis2) or len(napis2) > 3 * len(napis1):
			licznik += 1
			if pierwsza_para is None:
				pierwsza_para = (napis1, napis2)
	return licznik, pierwsza_para

def zadanie_2(lista_napisow):
	wyniki = []
	for napisy in lista_napisow:
		napis1, napis2 = napisy
		if napis2.startswith(napis1):
			roznica = napis2[len(napis1):]
			wyniki.append((napis1, napis2, roznica))
	return wyniki

def zadanie_3(lista_napisow):
	maks = 0
	lista = []
	for napisy in lista_napisow:
		napis1, napis2 = napisy
		k = ile_yap_yap_yap(napis1, napis2)
		if k > maks:
			maks = k
			lista = [(napis1, napis2)]
		elif k == maks:
			lista.append((napis1, napis2))
	return maks, lista

def wykonaj_obliczenia(lista_napisow):
	wynik_1 = zadanie_1(lista_napisow)
	wynik_2 = zadanie_2(lista_napisow)
	wynik_3 = zadanie_3(lista_napisow)
	return wynik_1, wynik_2, wynik_3

def zapisz_wyniki(wynik_1, wynik_2, wynik_3):
	with open("wyniki.txt", "w") as plik:
		plik.write("Pierwsza para:\n")
		if wynik_1[1]:
			plik.write(f"{wynik_1[1][0]} {wynik_1[1][1]}\n")
		plik.write(f"Par znalezionych:\n{wynik_1[0]+2}\n\n")
		plik.write("72.2.\n")
		for napis1, napis2, roznica in wynik_2:
			plik.write(f"{napis1} {napis2} {roznica}\n")
		plik.write("\n")
		plik.write(f"72.3.\n{wynik_3[0]}\n")
		for napis1, napis2 in wynik_3[1]:
			plik.write(f"{napis1} {napis2}\n")

with open("napisy.txt") as plik:
	lista_napisow = [linia.split() for linia in plik.readlines()]

wyniki = wykonaj_obliczenia(lista_napisow)
zapisz_wyniki(*wyniki)
