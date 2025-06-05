budynki = list(map(int, input().split()))
widoczne = []
największa_wysokość = 0

for w in budynki:
    if w > największa_wysokość:
        największa_wysokość = w
        widoczne.append(w)

widoczne = map(str, widoczne)
print('>>'.join(widoczne))