_ = int(input())
_ = int(input())
promień = int(input())

liczba_punktów = 0
for dx in range(-promień, promień + 1):
    for dy in range(-promień, promień + 1):
        if dx * dx + dy * dy <= promień * promień:
            liczba_punktów += 1

print(liczba_punktów)