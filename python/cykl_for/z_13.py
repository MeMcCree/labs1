samogłoski = 'аяоёэеуюыиАЯОЁЭЕУЮЫИ'

linia = input()
słowo = ''
liczba = 0
w_akcencie = False
ostatnia_spacja = True

for litera in linia:
    if litera == ' ':
        if słowo != '':
            akcent_znaleziony = False
            for c in słowo:
                if c == 'ё' or c == 'Ё':
                    akcent_znaleziony = True
                    break
            if not akcent_znaleziony and słowo != '':
                liczba_samogłosek = 0
                for c in słowo:
                    if c in samogłoski:
                        liczba_samogłosek += 1
                if liczba_samogłosek > 0:
                    liczba += liczba_samogłosek - 1
            słowo = ''
        ostatnia_spacja = True
    else:
        słowo += litera
        ostatnia_spacja = False

if słowo != '':
    akcent_znaleziony = False
    for c in słowo:
        if c == 'ё' or c == 'Ё':
            akcent_znaleziony = True
            break
    if not akcent_znaleziony:
        liczba_samogłosek = 0
        for c in słowo:
            if c in samogłoski:
                liczba_samogłosek += 1
        if liczba_samogłosek > 0:
            liczba += liczba_samogłosek - 1

print(liczba)
