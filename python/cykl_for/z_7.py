n = int(input())
suma_dzielników = 0

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        suma_dzielników += i
        if n // i != i:
            suma_dzielników += n // i

print(suma_dzielników)