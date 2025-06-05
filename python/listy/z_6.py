n = int(input())

barwy = []
for i in range(n):
    barwy.append(input())

m = int(input())

for i in range(m):
    print(barwy[i % n])