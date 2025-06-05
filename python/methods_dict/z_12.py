ludzi = {}
linia = input()
while linia:
    imię, przedmiot = linia.split(' - ')
    if imię not in ludzi:
        ludzi[imię] = {}
    ludzi[imię][przedmiot] = ludzi[imię].get(przedmiot, 0) + 1
    linia = input()

for imię, przedmioty in ludzi.items():
    części = []
    for przedmiot, ilość in przedmioty.items():
        części.append(f'{przedmiot} ({ilość})')
    print(f'{imię}: {", ".join(części)}')