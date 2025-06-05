n = int(input())
zachowane = n

faktory = []
dzielnik = 2
for dzielnik in range(2, int(n ** 0.5) + 1):
    while n % dzielnik == 0:
        faktory.append(dzielnik)
        n //= dzielnik

    dzielnik += 1

if n > 1:
    faktory.append(n)

równa_się = ' * '.join([str(faktor) for faktor in faktory])
print(f"{zachowane} = {równa_się}")