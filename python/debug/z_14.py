a = float(input())
v = float(input())
zakręty = 0

eps = 0.1 ** 2
while a > v:
    a = ((a - v) ** 2 + v ** 2) ** 0.5
    zakręty += 1
    if a - v <= eps:
        break

print(zakręty)