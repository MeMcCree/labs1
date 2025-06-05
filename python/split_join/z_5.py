n = int(input())
liczby = [str(i - 2) for i in range(n, 13) if i % 2 == 0]
print(' '.join(liczby))