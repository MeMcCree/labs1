naczynia = []
obecne = set()

linia = input()
while linia:
    if linia == '-1':
        naczynia.append(obecne)
        obecne = set()
    else:
        obecne.add(int(linia))
    linia = input()

if obecne:
    naczynia.append(obecne)

wszystkie_cząstki = set()
powtórzone = set()

for i, naczynie in enumerate(naczynia):
    for cząstka in naczynie:
        if cząstka in wszystkie_cząstki:
            powtórzone.add(cząstka)
        else:
            wszystkie_cząstki.add(cząstka)

wynik = wszystkie_cząstki - powtórzone
print(*sorted(wynik))