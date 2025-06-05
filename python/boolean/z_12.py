a = input()
b = input()
c = input()

wynik = a * (a <= b and a <= c) + b * (b < a and b <= c) + c * (c < a and c < b)
print(wynik)