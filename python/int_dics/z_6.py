n = int(input())
sertyfikaty = {}

for _ in range(n):
    imię, dół, góra = input().split()
    sertyfikaty[imię] = (int(dół), int(góra))

wyniki = list(map(int, input().split()))
łącznie = sum(wyniki)

for imię, (dół, góra) in sertyfikaty.items():
    if dół <= łącznie <= góra:
        print(imię)
        break