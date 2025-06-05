n = int(input())
studenci = {}
for i in range(n):
    linia = input()
    indeks = linia.rfind(': ')
    część = linia[:indeks]
    wynik = int(linia[indeks + 2:])
    imię, moduł = część.split(' (')
    moduł = moduł[:-1]

    if imię not in studenci:
        studenci[imię] = {moduł: wynik}
    else:
        studenci[imię][moduł] = studenci[imię].get(moduł, 0) + wynik

for imię, moduły in studenci.items():
    if len(moduły) == 5 and sum(moduły.values()) >= 75:
        print(imię)