liczby = []

liczba = int(input())
while liczba:
    liczby.append(liczba)
    liczba = int(input())

n = len(liczby)
wynik = [liczba for liczba in liczby if liczba % n == 0]
print(wynik)