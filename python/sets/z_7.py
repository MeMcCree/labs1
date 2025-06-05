n = int(input())
nogi = []
for i in range(n):
    nogi.append(int(input()))

ponad_40 = set()
parzyste = set()
podz_przez_3 = set()

for x in nogi:
    if x > 40:
        ponad_40.add(x)

for x in nogi:
    if x % 2 == 0:
        parzyste.add(x)

for x in nogi:
    if x % 3 == 0:
        podz_przez_3.add(x)

dwa_zestawa = (ponad_40 & parzyste) ^ (ponad_40 & podz_przez_3) ^ (parzyste & podz_przez_3)
dwa_zestawa = set(x for x in dwa_zestawa if sum([x in s for s in [ponad_40, parzyste, podz_przez_3]]) == 2)

w_dwóch = set()
for x in nogi:
    suma = sum([x in z for z in [ponad_40, parzyste, podz_przez_3]])
    if suma == 2:
        w_dwóch.add(x)

print(*w_dwóch)
