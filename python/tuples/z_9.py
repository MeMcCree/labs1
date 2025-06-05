n = int(input())

wynik = []
for i in range(n + 1):
    if i >= 2:
        silnia = 1
        j = i
        while j > 0:
            silnia *= j
            j -= 2
    else:
        silnia = 1

    wynik.append((i, silnia))

print(wynik)