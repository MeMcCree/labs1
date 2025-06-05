n = int(input())
m = int(input())

pos = 0

x = int(input())
while x:
    if x > 0:
        pos += n
    else:
        pos -= m
    x = int(input())

print(pos)