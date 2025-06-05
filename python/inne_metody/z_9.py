dane = list(map(int, input().split()))
start, koniec = map(int, input().split())

if start > koniec:
    start, koniec = koniec, start

wynik = sum(dane[start:koniec])
print(wynik)