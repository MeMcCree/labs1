tys = 1_000
mil = 1_000_000

porządek = ['Cenozoic', 'Mesozoic', 'Paleozoic', 'Proterozoic', 'Archaea']
dct = {
    'Cenozoic': (0, 145 * mil),
    'Mesozoic': (145 * mil, 300 * mil),
    'Paleozoic': (300 * mil, 635 * mil),
    'Proterozoic': (635 * mil, 2800 * mil),
    'Archaea': (2800 * mil, 4500 * mil)
}

lat_temu = input()
while lat_temu:
    age = int(lat_temu) * tys
    for era in porządek:
        start, koniec = dct[era]

        if start <= age < koniec:
            print(era)
            break
    lat_temu = input()