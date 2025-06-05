n = int(input())
pi = 0.0

for i in range(n):
    t = (-1) ** i / (2 * i + 1)
    pi += t

pi *= 4
print(pi)