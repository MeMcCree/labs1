n = int(input())
linii = []

for i in range(n):
    linii.append(input())

m = int(input())

imiona = []
for i in range(m):
    imiona.append(input())

for imię in imiona:
    znaliezione = False
    for i in range(n):
        if imię in linii[i]:
            print(i + 1)
            znaliezione = True
            break

    if not znaliezione:
        print(-1)