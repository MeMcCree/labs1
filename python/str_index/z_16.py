słowo = input()

pierwsze = słowo[0]
średnie = słowo[len(słowo) // 2]
przedostatnie = słowo[-2]
ostatnie = słowo[-1]

if pierwsze.islower():
    pierwsze = chr(ord('a') + (ord(pierwsze) - ord('a') + 23) % 26)
else:
    pierwsze = chr(ord('A') + (ord(pierwsze) - ord('A') + 23) % 26)

if średnie.islower():
    średnie = chr(ord('a') + (ord(średnie) - ord('a') + 23) % 26)
else:
    średnie = chr(ord('A') + (ord(średnie) - ord('A') + 23) % 26)

if przedostatnie.islower():
    przedostatnie = chr(ord('a') + (ord(przedostatnie) - ord('a') + 23) % 26)
else:
    przedostatnie = chr(ord('A') + (ord(przedostatnie) - ord('A') + 23) % 26)

if ostatnie.islower():
    ostatnie = chr(ord('a') + (ord(ostatnie) - ord('a') + 23) % 26)
else:
    ostatnie = chr(ord('A') + (ord(ostatnie) - ord('A') + 23) % 26)

wynik = pierwsze + średnie + przedostatnie + ostatnie
print(wynik)