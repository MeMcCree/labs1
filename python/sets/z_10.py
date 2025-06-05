n = int(input())
składniki = set()

for i in range(n):
    m = int(input())

    for j in range(m):
        składniki.add(input())

print(*składniki, sep='\n')