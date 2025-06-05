n, m, i, j, f = map(int, [input() for i in range(5)])

macierz = [[0] * n for i in range(m)]
macierz[j][i] = f
k = 0
while (t := int(f ** .5)) ** 2 == f and f != 1:
    k += 1
    f = t
    x4, y4 = i + k, j + k
    x1, y1 = i - k, j - k 
    for p in range(2 * k + 1):
        if 0 <= x1 + p < n and 0 <= y1 < m:
            macierz[y1][x1 + p] = f
        if 0 <= x1 < n and 0 <= y1 + p < m:
            macierz[y1 + p][x1] = f
        if 0 <= x4 - p < n and 0 <= y4 < m:
            macierz[y4][x4 - p] = f
        if 0 <= x4 < n and 0 <= y4 - p < m:
            macierz[y4 - p][x4] = f
 
[print(*rząd, sep='\t') for rząd in macierz]