liczba_siódemek = 0

while True:
    numer = int(input())
    
    if numer <= 0:
        break

    while numer:
        liczba_siódemek += (numer % 8 == 7)
        numer //= 8

print(liczba_siódemek)