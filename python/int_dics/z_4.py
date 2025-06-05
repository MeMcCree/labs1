n = int(input())
liczba_barw = {}

for _ in range(n):
    row = input().split("\t")
    for piksel in row:
        barwa = tuple(map(int, piksel.split()))
        liczba_barw[barwa] = liczba_barw.get(barwa, 0) + 1

maksymalna_liczba = max(liczba_barw.values())
for barwa, liczba in liczba_barw.items():
    if liczba == maksymalna_liczba:
        print(*barwa)