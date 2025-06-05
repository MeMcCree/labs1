n = int(input())

last = 0

while n:
    last = n % 12
    n = n // 12

print(last)