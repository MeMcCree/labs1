n = int(input())

zamówienia = []
for _ in range(n):
    zamówienia.append(input())

wynik = []

while zamówienia:
    ilość = 0
    rzecz = zamówienia[0]
    
    i = 0
    while i < len(zamówienia):
        if rzecz == zamówienia[i]:
            ilość += 1
            zamówienia.pop(i)
        else:
            i += 1
    
    wynik.append((ilość, rzecz))

for zamówienie in wynik:
    print(zamówienie)