linia = input()
pierwszy_indeks = linia.find("сосна")
ostatni_indeks = linia.rfind("сосна")

wynik = linia[pierwszy_indeks + len("сосна"):ostatni_indeks].strip()
print(wynik)