linia = input()

dlina = len(linia)
granica = dlina // 2
liczby = dict()
for length in range(1, granica + 1):
    for i in range(dlina - length + 1):
        t = linia[i:i + length]
        if not t in liczby:
            liczby[t] = 0
        liczby[t] += 1

for t, l in liczby.items():
    if l > 1:
        print(f'{t}: {l}')