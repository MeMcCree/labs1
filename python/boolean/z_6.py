ostatnia_linia_z_gwiazdą = None
spadająca_gwiazda_wykryta = False

numer_linii = 1
while True:
    linia = input().strip()
    
    if linia == "ВСЁ":
        break

    if "Звезд" in linia or "звезд" in linia:  
        spadająca_gwiazda_wykryta = False
        ostatnia_linia_z_gwiazdą = numer_linii
    if "пал" in linia or "пад" in linia:
        spadająca_gwiazda_wykryta = True
    
    numer_linii += 1

if ostatnia_linia_z_gwiazdą is None or spadająca_gwiazda_wykryta:
    print("НЕТ")
else:
    print(ostatnia_linia_z_gwiazdą)