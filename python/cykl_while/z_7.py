n = int(input())

ans = set()

i = 1
while i <= int(n ** 0.5) + 1:
    if n % i == 0:
        ans.add(i)
        ans.add(n // i)
    i += 1

ans = list(ans)
ans.sort()

i = 0
while i < len(ans):
    print(ans[i])
    i += 1