zdanie = input()
słowa = zdanie.split()
maksymalna_wysokość = max((len(słowo) - 1) // 2 + 1 for słowo in słowa)
wynik = [[] for _ in range(maksymalna_wysokość)]

for słowo in słowa:
    n = len(słowo)
    z = (n - 1) // 2
    linii_ze_słowami = []
    linii_ze_słowami.append(' ' * z + słowo[z:z + (n - 1) % 2 + 1])

    for i in range(1, z + 1):
        t = (z - i) * ' ' + słowo[z - i] + ' ' * (2 * i - n % 2) + słowo[z + i + (n - 1) % 2]
        linii_ze_słowami.append(t)
    
    ofset = maksymalna_wysokość - len(linii_ze_słowami)
    for i in range(ofset):
        linii_ze_słowami.insert(0, ' ' * n)
    
    for i, linia in enumerate(linii_ze_słowami):
        wynik[i].append(linia.ljust(n))

for linia in wynik:
    print(' '.join(linia).rstrip())