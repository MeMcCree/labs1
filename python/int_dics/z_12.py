n = int(input())
organizacja_z_imienia = {}
organizacja_ze_strony = {}
organizacja_z_numeru = {}
organizacja_z_adresu = {}

for i in range(n):
    imię = input()
    strona = input()
    numer = input()
    adres = input()
    info = (imię, strona, numer, adres)
    organizacja_z_imienia[imię] = info
    organizacja_ze_strony[strona] = info
    organizacja_z_numeru[numer] = info
    organizacja_z_adresu[adres] = info

m = int(input())
for i in range(m):
    typ_szukania = input()
    znaczenie_szukania = input()
    if typ_szukania == 'imię':
        result = organizacja_z_imienia.get(znaczenie_szukania)
    elif typ_szukania == 'strona':
        result = organizacja_ze_strony.get(znaczenie_szukania)
    elif typ_szukania == 'numer':
        result = organizacja_z_numeru.get(znaczenie_szukania)
    else:
        result = organizacja_z_adresu.get(znaczenie_szukania)

    if result:
        print(*result, sep='\n')
    
    if i < m - 1:
        print('-' * 10)