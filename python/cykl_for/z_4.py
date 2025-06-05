start = int(input())
krok = int(input())
koniec = int(input())

while start >= koniec:
    print(f"Высота {start}")
    start -= krok

print("Глиссада")