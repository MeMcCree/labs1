n = int(input())

spotkania = {}
for i in range(n):
    imię, dzień, miesiąc = input().split(', ')
    spotkania.setdefault(miesiąc, []).append((int(dzień), imię))

docelowy_miesiąc = input()
wynik = []

if docelowy_miesiąc in spotkania:
    wynik = sorted(spotkania[docelowy_miesiąc], key=lambda x: (x[0], x[1]))
    for dzień, imię in wynik:
        print(imię)