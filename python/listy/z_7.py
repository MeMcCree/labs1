sny = []
sen = input()
while sen != '':
    sny.append(sen)
    sen = input()

start = int(input())
koniec = int(input())

maksymalna_długość = 0
najdłuższy_sen = ''
for i in range(start - 1, koniec):
    if i < len(sny):
        if len(sny[i]) > maksymalna_długość:
            maksymalna_długość = len(sny[i])
            najdłuższy_sen = sny[i]
    else:
        break

print(najdłuższy_sen)