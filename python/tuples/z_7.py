n = int(input())
for i in range(n):
    linia = input()
    
    for j in range(1, len(linia)):
        if linia[j] < linia[j - 1]:
            print((i, j))