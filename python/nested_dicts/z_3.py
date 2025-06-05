n = int(input())

macierz = []
for i in range(n):
    rząd = [int(x) for x in input().split(", ")]
    macierz.append(rząd)

główna_suma = 0
przeciw_suma = 0
for i in range(n):
    przeciw_suma += macierz[i][n - 1 - i]
    główna_suma += macierz[i][i]
    macierz[i][i], macierz[i][n - 1 - i] = macierz[i][n - 1 - i], macierz[i][i]

for rząd in macierz:
    linia_rzędu = map(str, rząd)
    print(" ".join(linia_rzędu))

print(główna_suma + przeciw_suma)