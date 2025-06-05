s = input()
unikalne_litery = set(s)
znaczenia_unicoda = [ord(char) for char in unikalne_litery]
minimalny_unicode = min(znaczenia_unicoda)
maksymalny_unicode = max(znaczenia_unicoda)

print(f"{minimalny_unicode}, {maksymalny_unicode}")

if len(unikalne_litery) <= 32:
    print("ХВАТИТ")
else:
    print("НЕ ХВАТИТ")