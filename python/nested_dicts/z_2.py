macierz = []
linia = input()
while linia:
    macierz.append([int(x) for x in linia.split()])
    linia = input()

rzędy = len(macierz)
kolumny = len(macierz[0])

transponowana = [[macierz[r][k] for r in range(rzędy)] for k in range(kolumny)]
for i in range(kolumny):
    transponowana[i].sort(reverse=i % 2)

wynik = [[transponowana[k][r] for k in range(kolumny)] for r in range(rzędy)]
for rząd in wynik:
    print("\t".join(map(str, rząd)))