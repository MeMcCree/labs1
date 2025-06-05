n = int(input())
słowa = []

for i in range(n):
    słowa.append(input())

dodatkowe_słowo = input()

znaleziono = 0
for i in range(n):
    if słowa[i] <= dodatkowe_słowo:
        znaleziono = i + 1

print(znaleziono)