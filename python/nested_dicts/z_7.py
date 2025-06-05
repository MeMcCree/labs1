import math

n = int(input())
pajączyna = []
for i in range(n):
    pajączyna.append(list(map(int, input().split())))

for i in range(n):
    for j in range(len(pajączyna[i])):
        if pajączyna[i][j] == 0:
            łącznie = 0
            liczba = 0
            if i > 0:
                łącznie += pajączyna[i - 1][j]
                liczba += 1

            if i < n - 1:
                łącznie += pajączyna[i + 1][j]
                liczba += 1
            
            if j > 0:
                łącznie += pajączyna[i][j - 1]
                liczba += 1
            
            if j < len(pajączyna[i]) - 1:
                łącznie += pajączyna[i][j + 1]
                liczba += 1
            
            pajączyna[i][j] = math.floor(łącznie / liczba)

for rząd in pajączyna:
    print(rząd)