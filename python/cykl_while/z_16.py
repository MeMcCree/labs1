a = float(input())
n = int(input())

sqrt2 = 2 ** 0.5

while n:
    a /= sqrt2
    n -= 1

print(a * a)