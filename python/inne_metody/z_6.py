n = int(input())

stos = []
for dzielnik in range(1, int(n ** 0.5) + 1):
    if n % dzielnik == 0:
        print(dzielnik, end=' ')
        if dzielnik != n // dzielnik:
            stos.append(n // dzielnik)
while len(stos):
    print(stos.pop(), end=' ')