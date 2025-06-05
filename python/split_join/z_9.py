podciąg = input()
słowa = input().split()
wynik = [słowo for słowo in słowa if podciąg in słowo]
print(*wynik)