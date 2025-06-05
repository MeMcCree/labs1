a = input()
b = input()
c = input()

klucz1 = (len(a), a)
klucz2 = (len(b), b)
klucz3 = (len(c), c)

minimum = min(klucz1, klucz2, klucz3)
_, wynik = minimum

print(wynik)