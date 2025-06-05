linii = []
linia = input()
while linia != '':
    linii.append(linia)
    linia = input()

username = input()
prefiks = '@' + username + ' '

wynik = []
for linia in linii:
    if linia.startswith(prefiks):
        treść = linia[len(prefiks):].capitalize()
        wynik.append(treść)

wynik.sort()
for linia in wynik:
    print(linia)