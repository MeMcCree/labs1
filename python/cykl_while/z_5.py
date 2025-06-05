x = int(input())
last_x = x

c = 0
while x:
    if x > last_x:
        c += 1

    last_x = x
    x = int(input())

print(c)