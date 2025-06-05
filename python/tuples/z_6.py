n = int(input())
fale = []

for i in range(n):
    line = input()
    *tekst, wynik = line.split()
    fale.append((' '.join(tekst), int(wynik)))

for i in range(n - 1):
    if fale[i][1] < fale[i + 1][1]:
        print((i + 1, fale[i][0]))