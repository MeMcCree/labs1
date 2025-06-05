bg = float(input())
dist = int(input())

g = max(bg - bg * 0.02 * dist, bg / 2)

print(g)