s = input()
n = int(input())

ans = 0

while ' ' not in s:
    if len(s) == n:
        ans += 1

    s = input()
    if ' ' in s:
        break
    n = int(input())

print(ans)    