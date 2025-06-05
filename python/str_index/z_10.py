wyrażenie = input().strip()

znak = 1
obecny_numer = 0
wynik = 0
for znaczek in wyrażenie:
    if znaczek.isdigit():
        obecny_numer = int(znaczek)
        wynik += znak * obecny_numer
    elif znaczek == '+':
        znak = 1
    elif znaczek == '-':
        znak = -1

print(wynik)