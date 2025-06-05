depozyt = int(input())
stawka = float(input())
lata = float(input())

całe_lata = int(lata)
część_roku = lata - całe_lata

r = 1 + stawka / 100
while całe_lata:
    depozyt *= r
    całe_lata -= 1

if część_roku > 0:
    depozyt *= 1 + część_roku / 100

print(f"{depozyt:.10f}")