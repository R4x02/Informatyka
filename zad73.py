def liczba_slow_z_podwojna_litera(nazwa_pliku):
	licznik = 0
	with open(nazwa_pliku) as plik:
		for slowo in plik:
			slowo = ''.join(filter(str.isalpha, slowo.strip().upper()))
			for j in range(len(slowo) - 1):
				if slowo[j] == slowo[j + 1]:
					licznik += 1
	return licznik

def czestotliwosc_liter(nazwa_pliku):
	czestotliwosc = [0] * 26
	suma = 0
	with open(nazwa_pliku) as plik:
		for linia in plik:
			for znak in linia.strip().upper():
				if 'A' <= znak <= 'Z':
					indeks = ord(znak) - ord('A')
					czestotliwosc[indeks] += 1
					suma += 1
	return [(chr(ord('A') + i), czestotliwosc[i], (100 * czestotliwosc[i] / suma) if suma > 0 else 0) for i in range(26)]

def najdluzszy_ciag_spolgloskowy(nazwa_pliku):
	najdluzsze = 0
	licznik = 0
	odpowiedz = ""
	with open(nazwa_pliku) as plik:
		slowa = plik.read().split()
	for slowo in slowa:
		ciag = 0
		s = 0
		for znak in slowo.upper():
			if znak in "AEIOUY":
				s = 0
			else:
				s += 1
				if s > ciag:
					ciag = s
		if ciag > najdluzsze:
			najdluzsze = ciag
			licznik = 1
			odpowiedz = slowo
		elif ciag == najdluzsze:
			licznik += 1
	return najdluzsze, licznik, odpowiedz

def zapisz_wyniki(nazwa_pliku, wynik_1, wynik_2, wynik_3):
	with open(nazwa_pliku, "w") as plik:
		plik.write(f"Liczba słów z podwójną literą: {wynik_1}\n")
		plik.write("Częstotliwość liter:\n")
		for litera, liczba, procent in wynik_2:
			plik.write(f"{litera}: {liczba} ({procent:.2f}%)\n")
		plik.write(f"\nNajdłuższy ciąg spółgłosek: {wynik_3[0]}\nLiczba słów: {wynik_3[1]}\nSłowo: {wynik_3[2]}\n")

nazwa_pliku = "dane.txt"
nazwa_wynikow = "wyniki.txt"
w_1 = liczba_slow_z_podwojna_litera(nazwa_pliku)
w_2 = czestotliwosc_liter(nazwa_pliku)
w_3 = najdluzszy_ciag_spolgloskowy(nazwa_pliku)
zapisz_wyniki(nazwa_wynikow, w_1, w_2, w_3)
