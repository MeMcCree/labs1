x = int(input())

prev = 0
prevprev = 0

i = 0
ans = 0
while x != -1:
    if i > 1:
        if prev > x and prev > prevprev:
            ans += 1

    prevprev = prev
    prev = x
    x = int(input())
    i += 1

print(ans)