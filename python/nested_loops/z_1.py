n = int(input())

numer = 1
for i in range(n):
    for j in range(n):
        print(numer, end='\t')
        numer += 1
    print()