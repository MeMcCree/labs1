n = int(input())
miejsca = []

for _ in range(n):
    wysokość = int(input())
    żelazo = float(input())
    miejsca.append((wysokość, żelazo))

for i in range(n):
    maksymalny_indeks = i
    for j in range(i + 1, n):
        if (miejsca[j][0] > miejsca[maksymalny_indeks][0] or
           (miejsca[j][0] == miejsca[maksymalny_indeks][0] and miejsca[j][1] > miejsca[maksymalny_indeks][1])):
            maksymalny_indeks = j
    miejsca[i], miejsca[maksymalny_indeks] = miejsca[maksymalny_indeks], miejsca[i]

for miejsce in miejsca:
    print(miejsce)