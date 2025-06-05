linia = input()

wynik = []
i = 0
while i < len(linia):
    obecny_znaczek = linia[i]
    
    if obecny_znaczek == '%':
        i += 1
        continue
    
    liczba = 1
    i += 1
    
    while i < len(linia) and linia[i] == obecny_znaczek:
        liczba += 1
        i += 1

    if liczba >= 2:
        wynik.append(obecny_znaczek)
    elif i < len(linia) and linia[i] == '%':
        liczba_procentów = 0
        while i < len(linia) and linia[i] == '%':
            liczba_procentów += 1
            i += 1
        if liczba_procentów >= 2:
            wynik.append(obecny_znaczek)

print("".join(wynik))