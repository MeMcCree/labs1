imiona = []
imię = input()
while imię:
    if imię not in imiona:
        imiona.append(imię)
    imię = input()
n = len(imiona)

dlina = imiona[:]
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(dlina[j]) > len(dlina[j + 1]):
            dlina[j], dlina[j + 1] = dlina[j + 1], dlina[j]

alfa = imiona[:]
for i in range(n - 1):
    for j in range(n - 1 - i):
        if alfa[j] > alfa[j + 1]:
            alfa[j], alfa[j + 1] = alfa[j + 1], alfa[j]

wynik = "YES"
for t, u in zip(alfa, dlina):
    if t != u:
        wynik = f"{t} {u}"
        break

print(wynik)
