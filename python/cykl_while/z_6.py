x = float(input())

n = 0
s = 0
while x:
    n += 1
    s += x
    x = float(input())

if n:
    print(s / n)
else:
    print(0)