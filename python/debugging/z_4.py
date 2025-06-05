r = float(input())
n = float(input())
m = float(input())

pos = 0
t = 0
while pos < r:
    pos += n
    n += m
    t += 1

print(t)