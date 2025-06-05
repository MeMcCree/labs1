k = int(input())
n = int(input())

schodki = ["БОСИКОМ" if i % k == 0 else str(i) for i in range(1, n + 1)]

print(", ".join(schodki))