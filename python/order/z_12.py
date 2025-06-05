from math import pi

r = float(input())
n = int(input())

v = 4 / 3 * pi * (r ** 3)
sum_v = v * n

# sum_v = (4/3)pi * R^3
# (sum_v*3)/4pi = R^3
# ((sum_v*3)/4pi) ** (1/3) = R
R = ((sum_v * 3) / 4 / pi) ** (1 / 3)

print(format(R, '.9f'))