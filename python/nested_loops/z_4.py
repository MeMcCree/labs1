s = int(input())

for i in range(1, s + 1):
    for j in range(1, i + 1):
        if i * j == s:
            print(i, j)