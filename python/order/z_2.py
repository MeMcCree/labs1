n = int(input())
m = int(input())

s = input()

cnt = len(s) // m + int(len(s) % m != 0)

print(cnt * n)