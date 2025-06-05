liczby = list(map(int, input().split()))

drzewo = [liczby]
while len(drzewo[0]) > 1:
    obecne = drzewo[0]
    następny_poziom = []
    for i in range(0, len(obecne), 2):
        prawe = 0 if i + 1 >= len(obecne) else obecne[i + 1]
        następny_poziom.append(obecne[i] + prawe)
    drzewo.insert(0, następny_poziom)

for poziom in drzewo:
    print(" ".join(list(map(str, poziom))))