a = int(input())
b = int(input())
c = int(input())
d = int(input())

n = b
k = d
while n != k:
    if k > n:
        n, k = k, n
    n -= k

lcm = b * d // k
a *= lcm // b
c *= lcm // d
a -= c

n = a
k = lcm
while n != k:
    if k > n:
        n, k = k, n
    n -= k

a //= k
lcm //= k

print(f"{a}/{lcm}")