liczba = int(input())
wynik = [str(int(n) ** 2) for n in ('1' * i for i in range(1, len(str(liczba)) + 1)) if int(n) <= liczba]
print(', '.join(wynik))