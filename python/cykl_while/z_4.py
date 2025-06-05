x = int(input())

a = -10000
b = -10000

i = 0
while abs(x) < 1000:
    if i % 2:
        if x > a:
            a = x
        elif x > b:
            b = x
    else:
        if x > b:
            b = x
        elif x > a:
            a = x

    i += 1
    x = int(input())

print(min(a, b))