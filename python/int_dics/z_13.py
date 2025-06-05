from math import factorial

słowa = input().split()
liczby = {}
for słowo in słowa:
    liczby[słowo] = liczby.get(słowo, 0) + 1

dliny_grup = {}
for słowo, liczba in liczby.items():
    dliny_grup.setdefault(len(słowo), []).append((słowo, liczba))

if len(dliny_grup) == 1:
    print(1)
else:
    lengths = sorted(dliny_grup)
    ros = 1
    for length in lengths:
        grupa = dliny_grup[length]
        k = sum(c for _, c in grupa)
        duplikaty = sum(c - 1 for _, c in grupa if c > 1)
        ros *= factorial(k - duplikaty)

    spad = 1
    for length in reversed(lengths):
        grupa = dliny_grup[length]
        k = sum(c for _, c in grupa)
        duplikaty = sum(c - 1 for _, c in grupa if c > 1)
        spad *= factorial(k - duplikaty)

    print(ros + spad)