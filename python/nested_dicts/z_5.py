n = int(input())
m = int(input())

macierz = []
for i in range(n):
    rząd = []
    for j in range(m):
        rząd.append(input())
    macierz.append(rząd)

for rząd in macierz:
    print("; ".join(rząd))
print()

transponowana = [[macierz[i][j] for i in range(n)] for j in range(m)]
for rząd in transponowana:
    print("; ".join(rząd))