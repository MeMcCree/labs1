słowa = []
słowo = input()
while słowo:
    słowa.append(słowo)
    słowo = input()

wynik = []
for słowo in słowa:
    częstość = {}
    for litera in słowo:
        częstość[litera] = częstość.get(litera, 0) + 1
    wynik.append([częstość[litera] for litera in słowo])

print(wynik)