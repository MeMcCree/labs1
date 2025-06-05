n = int(input())
k = int(input())

pos = True

i = 0
while n != k:
    n //= 2
    if n < k:
        print("IMPOSSIBLE")
        pos = False
        break
    i += 1

if pos:
    print(i)