n = int(input())
funkcje = []
for i in range(n):
    funkcje.append(set(input()))

wspólne = set.intersection(*funkcje)
łącznie = set.union(*funkcje)

print(len(wspólne), len(łącznie))