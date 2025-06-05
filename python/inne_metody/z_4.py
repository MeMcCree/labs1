separator = input()
słowa = input().split()

wynik = []
for słowo in słowa:
    przekształcone = separator.join(słowo.upper())
    wynik.append(przekształcone)

print(' '.join(wynik))