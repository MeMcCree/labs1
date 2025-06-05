cel = input()
n = int(input())

maksimum = 0
liczba = 0

for i in range(n):
    c = input()
    if c == cel:
        liczba += 1
        if liczba > maksimum:
            maksimum = liczba
    else:
        liczba = 0

print(maksimum)