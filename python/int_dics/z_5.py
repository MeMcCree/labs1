liczby = list(map(int, input().split()))
wynik = []

for liczba in liczby:
    binarna = bin(liczba)[2:]
    cyfry = len(binarna)
    jedynki = binarna.count('1')
    zera = binarna.count('0')
    wynik.append({'digits': cyfry, 'units': jedynki, 'zeros': zera})

print(wynik)