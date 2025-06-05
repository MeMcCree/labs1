n = int(input())
barwy = []

for i in range(n):
    m = int(input())

    for j in range(m):
        barwy.append(input())

liczby_barw = {}
for barwa in barwy:
    liczby_barw[barwa] = liczby_barw.get(barwa, 0) + 1

powtórzone = 0
for liczba in liczby_barw.values():
    if liczba > 1:
        powtórzne += 1

powtórzone = 0
for liczba in liczby_barw.values():
    if liczba > 1:
        powtórzone += 1

lącznie_powtórzonych = 0
for liczba in liczby_barw.values():
    if liczba > 1:
        lącznie_powtórzonych += liczba

print(powtórzone, lącznie_powtórzonych)