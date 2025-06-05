a = int(input())
b = int(input())

rzędy = min(a, b)
kolumny = max(a, b)

licznik = 1
for rząd in range(rzędy):
    if rząd % 2 == 0:
        for i in range(kolumny):
            print(licznik, end='\t')
            licznik += 1
    else:
        start = licznik + kolumny - 1

        for i in range(kolumny):
            print(start, end='\t')
            start -= 1
        
        licznik += kolumny
    print()