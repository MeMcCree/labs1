n = int(input())

suma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        potęga = i * (i + 2) // 4
    else:
        potęga = (i + 1) ** 2 // 4
    
    suma += i ** potęga

print(suma)