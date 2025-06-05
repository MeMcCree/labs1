import math

h = int(input())
m = int(input())

hdeg = (h % 12) * 2 * math.pi / 12 + m * 2 * math.pi / 60 / 12
mdeg = m * 2 * math.pi / 60

delta = hdeg - mdeg
if (delta < 0):
	delta = -delta

print(f"{delta / math.pi * 180:.8f}") 