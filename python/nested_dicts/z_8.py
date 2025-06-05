n = int(input())

macierz = []
for i in range(n):
    macierz.append(list(map(int, input().split())))
m = len(macierz[0])

łącznie = sum(macierz[0]) + sum(macierz[-1])
for i in range(1, n - 1):
    łącznie += macierz[i][0] + macierz[i][-1]

centralny_rząd = n // 2
centralna_kolumna = m // 2
macierz[centralny_rząd][centralna_kolumna] = łącznie
for rząd in macierz:
    print('\t'.join(list(map(str, rząd))))