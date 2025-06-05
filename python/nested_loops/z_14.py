lącznie_zwierząt = int(input())
łacznie_koszt = int(input())

for gęś in range(łacznie_koszt // 25 + 1):
    maksymum_kaczek = (łacznie_koszt - gęś * 25) // 10

    for kaczka in range(maksymum_kaczek + 1):
        kurczak = lącznie_zwierząt - gęś - kaczka
        if kurczak >= 0 and gęś * 25 + kaczka * 10 + kurczak * 7 == łacznie_koszt:
            print(gęś, kaczka, kurczak)