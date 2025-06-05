n = int(input())

liczby = []
for i in range(n):
    liczby.append(int(input()))

suma_łącznie = 0
for numer in liczby:
    suma_łącznie += numer

wynik = []
usunięta_suma = 0
for numer in liczby:
    if numer % 2 == suma_łącznie % 2:
        wynik.append(numer)
    else:
        usunięta_suma += numer

print(usunięta_suma, wynik)
