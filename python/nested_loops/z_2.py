start = int(input())
koniec = int(input())
krok = int(input())

for i in range(start, koniec + 1, krok):
    for j in range(start, koniec + 1, krok):
        print(f"{i} + {j} = {i + j}", end='\t')
    print()