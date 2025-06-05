rn = int(input())
fn = int(input())
n = int(input())

for i in range(n):
    r = int(input())
    f = fn * rn ** 2 / r ** 2
    print(('№' + str(i + 1), f))