n = int(input())
cyfry = set()
# Ciekawy czy twój numer jest aktywny, bo pamiętam niektóre jego cyfry...

for i in range(n):
    numer = input()
    cyfry.update(numer)

print(len(cyfry))