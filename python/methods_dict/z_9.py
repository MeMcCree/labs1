rzymskie_liczby = {
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
}

n = int(input())
wynik = []
for znaczenie in sorted(rzymskie_liczby.keys(), reverse=True):
    ilość = n // znaczenie
    if ilość:
        wynik.append(rzymskie_liczby[znaczenie] * ilość)
        n -= znaczenie * ilość

print(''.join(wynik))