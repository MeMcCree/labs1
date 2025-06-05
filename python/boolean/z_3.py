znaleziono = False
numer_linii = 1

while True:
    linia = input()
    
    if linia == "ВСЁ":
        break
    
    if "Звезд" in linia or "звезд" in linia:
        print(numer_linii)
        znaleziono = True
        break

    numer_linii += 1

if not znaleziono:
    print("НЕТ")