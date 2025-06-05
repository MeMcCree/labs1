n = int(input())

wynik = ''
for i in range(1, n + 1):
    słowo = input()

    if i <= len(słowo):
        wynik += słowo[-i]
    else:
        wynik = None
        break

if wynik is not None:
    print(wynik)
else:
    print("None")