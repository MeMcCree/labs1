n = int(input())

linii = []
for i in range(n):
    linii.append(input())

m = int(input())

zapytanie = []
for i in range(m):
    zapytanie.append(input())

for linia in linii:
    ma_wszystko = True
    for słowo in zapytanie:
        znalezione = False
        słowa = linia.split(' ')
        słowa = filter(lambda x: len(x), słowa)

        for słowo_w_linii in słowa:
            if słowo_w_linii == słowo:
                znalezione = True
                break

        if not znalezione:
            ma_wszystko = False
            break
    
    if ma_wszystko:
        print(linia)