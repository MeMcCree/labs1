import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

print(math.gcd(dx, dy) + 1)