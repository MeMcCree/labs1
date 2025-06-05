k = int(input())

znaczenia = []
while len(znaczenia) < k * 11:
    znaczenia.append(int(input()))

minimalna_ocena = 0
minimalna_średnia = None
maksymalna_ocena = 0
maksymalna_średnia = None

for i in range(11):
    łącznie = 0
    ilość = 0
    
    for j in range(k):
        u = znaczenia[j * 11 + i]
        
        if u > 0:
            ilość += 1
            łącznie += u

    if ilość == 0:
        continue
    
    średnia = łącznie / ilość
    if minimalna_średnia is None or średnia < minimalna_średnia:
        minimalna_ocena = i + 1
        minimalna_średnia = średnia
    if maksymalna_średnia is None or średnia > maksymalna_średnia:
        maksymalna_ocena = i + 1
        maksymalna_średnia = średnia

print(minimalna_ocena, maksymalna_ocena)
