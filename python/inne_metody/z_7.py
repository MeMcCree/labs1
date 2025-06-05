import re

linia = input()
poziom = int(input())

if poziom <= 100:
    linia = re.sub(r'\|\|\|', '00', linia, count=3)
else:
    linia = re.sub(r'0000', '|||', linia)

wynik = re.sub(r'\|0\|', '|00|', linia, count=1)

print(wynik)