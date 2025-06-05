n = int(input())
m = abs(n)

wynik = 1
i = 2
while i * i <= m:
    if m % i == 0:
        wynik *= i
        while m % i == 0:
            m //= i
    if i == 2:
        i += 1
    else:
        i += 2

if m > 1:
    wynik *= m

print(wynik)