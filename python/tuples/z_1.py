numery = []
x = int(input())
while x:
    numery.append(x)
    x = int(input())

for i in range(len(numery)):
    maksymalny_indeks = i
    for j in range(i + 1, len(numery)):
        if numery[j] > numery[maksymalny_indeks]:
            maksymalny_indeks = j
    numery[i], numery[maksymalny_indeks] = numery[maksymalny_indeks], numery[i]

numery = map(str, numery)
wynik = '->'.join(numery)

print(wynik)