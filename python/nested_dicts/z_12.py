n = int(input())
m = int(input())

rośliny = []
for i in range(m):
    rośliny.append(input())
rośliny.sort(key=lambda x: (len(x), x))

łóżka = [[] for _ in range(n)]
for i, roślina in enumerate(rośliny):
    łóżka[i % n].append(roślina)

for łóżko in łóżka:
    print(", ".join(łóżko))