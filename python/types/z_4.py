n = int(input())

d = n % 10
c = n % 100 // 10
b = n % 1000 // 100
a = n // 1000

if (a > b and b != 0):
	a, b = b, a

if (a > c and c != 0):
	a, c = c, a

if (a > d and d != 0):
	a, d = d, a

if (b > c):
	b, c = c, b

if (b > d):
	b, d = d, b

if (c > d):
	c, d = d, c

print(str(a) + str(b) + str(c) + str(d))