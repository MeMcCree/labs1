n = int(input())

lista_cyfr = []
lista_wyników = []
lista_cyfr.extend(str(n))
lista_wyników.extend(str(n))

obecna_suma = 0
tymczasowy_numer = 0
while len(str(n)) >= len(str(tymczasowy_numer)) and n != tymczasowy_numer:
    obecna_suma = 0
    for cyfra in lista_cyfr:
        obecna_suma += int(cyfra)

    tymczasowy_numer = obecna_suma
    lista_wyników.append(obecna_suma)
    lista_cyfr.pop(0)
    lista_cyfr.append(tymczasowy_numer)

if n != tymczasowy_numer:
    print('NO')
else:
    print(*lista_wyników)