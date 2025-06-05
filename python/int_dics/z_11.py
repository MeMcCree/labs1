# półżycia - całe życie konsekwencje
półżycia_linia = input().split()
dystrybucja = input().split()
aktywności = list(map(float, input().split()))
granica = float(input())

ilość_półżyć = {}
for i in range(0, len(półżycia_linia), 2):
    ilość_półżyć[półżycia_linia[i]] = int(półżycia_linia[i + 1])

obecne_aktywności = aktywności[:]

dni = 0
while sum(obecne_aktywności) > granica:
    dni += 1
    for i, element in enumerate(dystrybucja):
        if dni % ilość_półżyć[element] == 0:
            obecne_aktywności[i] /= 2

print(dni)
print(' '.join(str(a) for a in obecne_aktywności))