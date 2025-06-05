kontrolny = input()
n = int(input())

maksymalna_różnica = 0
wynik = set()

for i in range(n):
    linia = input()
    różnica = set(linia) - {kontrolny}
    
    if len(różnica) > maksymalna_różnica:
        maksymalna_różnica = len(różnica)
        wynik = różnica

if maksymalna_różnica != 0:
    print(''.join(sorted(wynik)))
else:
    print(-1)