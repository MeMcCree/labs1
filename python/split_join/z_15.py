linii = input().split()
maks_słowo = ''
słowo_indeksa = ''
maks_dlina_słowa = 0
wynik = []

for i in range(len(linii)):
    if len(linii[i]) > maks_dlina_słowa:
        maks_słowo = linii[i]
        maks_dlina_słowa = len(linii[i])

for indeks_słowa in range(maks_dlina_słowa):
    for string in linii:
        if indeks_słowa >= len(string):
            słowo_indeksa += ' '
            continue
        else:
            słowo_indeksa += string[indeks_słowa]
    
    wynik.append(słowo_indeksa)
    słowo_indeksa = ''

for i in range(len(wynik)):
    if i == 0:
        wynik[i] = '_' + '_'.join(wynik[i]) + '_'
    else:
        wynik[i] = ' ' + ' '.join(wynik[i])

print(*wynik, sep='\n')
print()
print(*wynik[::-1], sep='\n')