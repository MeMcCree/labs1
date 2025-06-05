linia = input().strip()
ilości = {}
wynik = []

for litera in linia:
    ilości[litera] = ilości.get(litera, 0) + 1
    wynik.append(str(ilości[litera]))

print(' '.join(wynik))