n = int(input())
wynik = [f'{i}, ' if i % 4 != 0 else f'{i}; АХ! ' for i in range(1, n + 1)]
print(''.join(wynik).rstrip(', '))