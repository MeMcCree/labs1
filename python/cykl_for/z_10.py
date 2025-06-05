n = int(input())
m = int(input())

for i in range(n, m + 1):
    s = str(i)

    if len(s) == 4 and all(s.count(litera) == 1 for litera in s):
        print(i)