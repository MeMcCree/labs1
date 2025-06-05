litera = input()

wynik = ''
if 'A' <= litera <= 'Z':
    wynik = chr(ord(litera) + 32)
elif 'a' <= litera <= 'z':
    wynik = chr(ord(litera) - 32)

print(wynik)