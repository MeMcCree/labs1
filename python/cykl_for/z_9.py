n = int(input())
pierścienie = []

for i in range(n, -1, -1):
    pierścienie.append(str(i))

print(*pierścienie, sep=' -> ')