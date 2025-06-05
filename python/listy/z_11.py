linii_tekstu = []
obecna_linia = input()
while '</html>' not in obecna_linia:
    linii_tekstu.append(obecna_linia)
    obecna_linia = input()

obecny_indeks_paragrafu = 0
paragraf_otwarty = False
paragrafy = []
for linia in linii_tekstu:
    if '<p>' in linia and '</p>' in linia:
        content = linia[linia.find('<p>') + 3:linia.find('</p>')]
        paragrafy.append(content)
        continue
    
    if '</p>' in linia and '<p>' not in linia:
        content = linia[:linia.find('</p>')]
        paragrafy[obecny_indeks_paragrafu] += content
        paragraf_otwarty = False
        continue

    if '<p>' in linia and '</p>' not in linia:
        content = linia[linia.find('<p>') + 3:] + ' '
        paragrafy.append(content)
        obecny_indeks_paragrafu = len(paragrafy) - 1
        paragraf_otwarty = True
        continue 
    
    if paragraf_otwarty:
        paragrafy[obecny_indeks_paragrafu] += linia + ' '
        continue

for paragraf in paragrafy[::-1]:
    print(paragraf)