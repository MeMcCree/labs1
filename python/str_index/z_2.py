alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
start = (n - 1) % 26

if start + 4 <= 26:
    wynik = alfabet[start:start + 4]
else:
    wynik = alfabet[start:] + alfabet[:(start + 4) % 26]

print(wynik)