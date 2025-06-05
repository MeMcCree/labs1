n = int(input())

faktory = [2, 3, 5]
numer = 1
znaleziony = 0
while znaleziony < n:
    numer += 1
    x = numer
    
    for faktor in faktory:
        while x % faktor == 0:
            x //= faktor

    if x == 1:
        znaleziony += 1

print(numer)