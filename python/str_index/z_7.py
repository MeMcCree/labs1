słowo = input()

wynik = ''
for i, litera in enumerate(słowo, 1):
    wynik += litera * i

print(wynik)