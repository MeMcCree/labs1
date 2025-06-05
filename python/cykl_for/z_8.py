n = int(input())
słowa = [] 

for i in range(n):
    słowa.append(input())

print(*słowa, sep='_', end='')