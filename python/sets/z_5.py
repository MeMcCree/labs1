n = int(input())
baza1 = set()
for i in range(n):
    baza1.add(input())

n = int(input())
baza2 = set()
for i in range(n):
    baza2.add(input())

wspólne = baza1 & baza2

for numer in wspólne:
    print(numer)