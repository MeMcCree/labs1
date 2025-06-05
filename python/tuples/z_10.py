angielski_alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ruski_alfabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

tekst = input()
wynik = set()

for litera in tekst:
    pozycja = angielski_alfabet.find(litera)
    if pozycja == -1:
        pozycja = ruski_alfabet.find(litera)

    if pozycja != -1:
        wynik.add((litera, pozycja))

print(*wynik, sep='\n', end='')