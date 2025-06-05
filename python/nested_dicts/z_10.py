drogi = []
droga = input()
while droga:
    drogi.append(droga)
    droga = input()
miasta = sorted(set(droga[0] for droga in drogi) | set(droga[1] for droga in drogi))

n = len(miasta)
macierz = [[0] * n for i in range(n)]
for droga in drogi:
    i = miasta.index(droga[0])
    j = miasta.index(droga[1])
    macierz[i][j] = 1

print(' ', *miasta)
for i in range(n):
    print(miasta[i], *macierz[i])