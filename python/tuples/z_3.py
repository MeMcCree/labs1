życzenia = []

życzenie = input()
while życzenie != 'разбитое корыто':
    życzenia.append(życzenie)
    życzenie = input()

n = len(życzenia)

for i in range(n):
    minimalny_indeks = i
    for j in range(i + 1, n):
        if len(życzenia[j]) < len(życzenia[minimalny_indeks]):
            minimalny_indeks = j
    życzenia[i], życzenia[minimalny_indeks] = życzenia[minimalny_indeks], życzenia[i]

for życzenie in życzenia:
    print(życzenie)