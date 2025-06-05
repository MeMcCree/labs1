znaczek = input()
n = int(input())

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(znaczek, end=' ')
        else:
            print('  ', end='')
    print()