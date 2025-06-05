linii = []
linia = input()
while linia != '':
    linii.append(linia)
    linia = input()

maksymalna_dlina = 0
for linia in linii:
    if len(linia) > maksymalna_dlina:
        maksymalna_dlina = len(linia)

wynik = []
for linia in linii:
    łacznie_kresek = maksymalna_dlina - len(linia)
    lewe_kreski = łacznie_kresek // 2
    prawe_kreski = łacznie_kresek - lewe_kreski
    przekształcona = '-' * lewe_kreski + linia + '-' * prawe_kreski
    wynik.append(przekształcona)

for przekształcona in wynik[::-1]:
    print(przekształcona)