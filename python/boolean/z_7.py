mile = int(input())
liczba = 1

for i in range(mile):
    if liczba % 7 == 0:
        print("Крюк!")
        liczba = 1
    else:
        print(f"Пройдена {liczba} миля.")
        liczba += 1